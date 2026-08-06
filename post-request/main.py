from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define the Data Model
class PredictionRequest(BaseModel):
    model_name: str
    input_data: list[float]
    threshold: float = 0.5  # Default value if not provided

# 2. Create the POST Endpoint
@app.post("/predict/")
async def run_prediction(request: PredictionRequest):
    # Access the validated data using dot notation
    name = request.model_name
    data = request.input_data
    
    # Process the data (mock logic)
    result_length = len(data)
    
    # Return a JSON response
    return {
        "status": "success",
        "model_used": name,
        "processed_features": result_length,
        "applied_threshold": request.threshold
    }