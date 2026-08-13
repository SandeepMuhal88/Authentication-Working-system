import random
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import engine, get_db, User, OTPRecord
from auth import create_access_token, get_current_user

app = FastAPI(title="Mobile OTP Authentication")

# --- Pydantic Schemas ---
class PhoneRequest(BaseModel):
    phone_number: str

class VerifyOTPRequest(BaseModel):
    phone_number: str
    otp: str

# --- Helper: Mock SMS Sender ---
def send_sms(phone_number: str, otp: str):
    # IN PRODUCTION: Integrate Twilio, AWS SNS, or Firebase here
    print(f"*** SIMULATED SMS to {phone_number} - Your OTP is: {otp} ***")

# --- Routes ---

@app.post("/send-otp")
def send_otp(request: PhoneRequest, db: Session = Depends(get_db)):
    # 1. Generate a 6-digit random OTP
    otp_code = str(random.randint(100000, 999999))
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=5)

    # 2. Save or update the OTP in the database
    existing_otp = db.query(OTPRecord).filter(OTPRecord.phone_number == request.phone_number).first()
    if existing_otp:
        existing_otp.otp = otp_code
        existing_otp.expires_at = expiration_time
    else:
        new_otp = OTPRecord(
            phone_number=request.phone_number,
            otp=otp_code,
            expires_at=expiration_time
        )
        db.add(new_otp)
    
    db.commit()

    # 3. Send the SMS
    send_sms(request.phone_number, otp_code)

    return {"message": "OTP sent successfully"}

@app.post("/verify-otp")
def verify_otp(request: VerifyOTPRequest, db: Session = Depends(get_db)):
    # 1. Look up the OTP record
    otp_record = db.query(OTPRecord).filter(OTPRecord.phone_number == request.phone_number).first()
    
    if not otp_record or otp_record.otp != request.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
        
    # Using naive datetime matching for simplicity in SQLite, in prod ensure timezone awareness aligns
    if otp_record.expires_at < datetime.now(timezone.utc):
        db.delete(otp_record)
        db.commit()
        raise HTTPException(status_code=400, detail="OTP has expired")

    # 2. Check if user exists; if not, CREATE them and assign an ID
    user = db.query(User).filter(User.phone_number == request.phone_number).first()
    if not user:
        user = User(phone_number=request.phone_number)
        db.add(user)
        db.commit()
        db.refresh(user) # Refreshes to get the newly generated UUID

    # 3. Clean up the used OTP
    db.delete(otp_record)
    db.commit()

    # 4. Generate JWT Token using the user's assigned ID
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user_id": user.id
    }

@app.get("/users/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    # This route is protected. It requires a valid Bearer token.
    return {
        "id": current_user.id,
        "phone_number": current_user.phone_number,
        "status": "Authenticated successfully!"
    }