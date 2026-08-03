from fastapi import FastAPI
from mockdata import products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API!"}

@app.get("/products")
def get_products():
    return products

