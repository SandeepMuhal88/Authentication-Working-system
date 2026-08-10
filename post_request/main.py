from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/create_product")
def create_product():
    return {"message": "Product created successfully!"}


@app.post("/create_order")
def create_order(request: Request):
    order_data = request.json()
    return {"message": "Order created successfully!", "order_data": order_data}

