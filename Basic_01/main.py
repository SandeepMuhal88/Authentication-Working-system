from fastapi import FastAPI, Request
from mockdata import data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API!"}


@app.get("/students")
def get_students():
    return data

@app.get("/student/{student_id}")
def get_student(student_id: int):
    for student in data:
        if student["id"] == student_id:
            return student
    
    return {"error": "Student not found."}
    
