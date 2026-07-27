from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt # PyJWT library
from datetime import datetime, timedelta

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"

# Mock Database
fake_users_db = {
    "user1": {
        "username": "user1",
        "hashed_password": "fakehashedpassword" # In production, use bcrypt or passlib
    }
}

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    # Sign the JWT token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. Verification
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict or form_data.password != "password": # Simplified check
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # 2. Token Generation
    access_token = create_access_token(data={"sub": user_dict["username"]})
    
    # 3. Token Delivery
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected-data")
async def read_protected_data(token: str = Depends(oauth2_scheme)):
    # 4. Validation happens automatically via Depends(oauth2_scheme)
    # Here we decode to get the user ID
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
    return {"message": f"Hello {username}, you have access to this data."}