from fastapi import FastAPI,Request
from mockdata import products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API!"}

@app.get("/products")
def get_products():
    return products


#Path params

@app.get("/product/{product_id}")
def get_product(product_id:int):
    for product in products:
        if product["id"] == product_id:
            return product
    
    return {"error": "Product not found."}



#Query params

# @app.get("/greet")
# def greet_user(name:str,age:int):
#     return {"message": f"Hello, {name}! You are {age} years old."}

# @app.get("/greet")
# def greet_user(request:Request):
#     query_params = dict(request.query_params)
#     # print(query_params)


#     return {
#         "message": f"Hello, {query_params.get("name")}, your age is {query_params.get("age")}!",
#     }



@app.get("/greet")
def greet_user(name:str,age:int):
    return {
        "message": f"Hello, {name}, your age is {age}!",
    }

@app.get("/search")
def search_products(query:str):
    results = [product for product in products if query.lower() in product["name"].lower()]
    return results


@app.post("/products")
def create_product(product: dict):
    new_product = {
        "id": len(products) + 1,
        "name": product.get("name"),
        "price": product.get("price"),
    }
    products.append(new_product)
    return new_product
    

