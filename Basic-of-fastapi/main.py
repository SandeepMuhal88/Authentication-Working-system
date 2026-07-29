# import fastapi

# print(fastapi.__version__)


from fastapi import FastAPI
app=FastAPI()


app.get("/")(lambda: {"message": "Hello World"})

app.get("/items/{item_id}")(lambda item_id: {"item_id": item_id})

