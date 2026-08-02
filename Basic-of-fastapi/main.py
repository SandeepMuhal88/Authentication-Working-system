
# import fastapi

# print("FastAPI version:", fastapi.__version__)


# from fastapi import FastAPI

# from fastapi import FastAPI, Depends, HTTPException, status
# from pydantic import BaseModel, Field, EmailStr

# email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# name_regex = r"^[a-zA-Z]+$"

# age_regex = r"^\d+$"



# app=FastAPI()


# app.get("/")(lambda: {"message": "Hello World"})

# app.get("/items/{item_id}")(lambda item_id: {"item_id": item_id})

# app.get("/users/{user_id}")(lambda user_id: {"user_id": user_id})
# app.get("/users/{user_id}/items/{item_id}")(lambda user_id, item_id: {"user_id": user_id, "item_id": item_id})
# app.get("/users/{user_id}/items/{item_id}")(lambda user_id, item_id: {"user_id": user_id, "item_id": item_id})


# app.get("/users/{user_id}/items/{item_id}")(lambda user_id, item_id: {"user_id": user_id, "item_id": item_id})

# app.post("/users/")(lambda user: {"user": user})

# app.patch("/users/{user_id}")(lambda user_id, user: {"user_id": user_id, "user": user})


from fastapi import FastAPI

app =FastAPI()

