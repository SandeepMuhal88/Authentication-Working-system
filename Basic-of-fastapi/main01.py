from fastapi import FastAPI

app =FastAPI()


@app.get("/")
def home():
    return {"message": "This is the home page of the FastAPI application."}




@app.get("/contact")
def contact():
    return {"message": "You can contact us at using the contact form on our website."}


@app.get("/about")
def about():
    return {"message": "This is the about page of the FastAPI application."}


# @app.get("")

def get_products():
    return {"message": "This is the products page of the FastAPI application."}