from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    id: int
    name: str
    grade: int

#create a list of students
students = [
    Student(id=1, name="John", grade=85),
    Student(id=2, name="Jane", grade=90),
    Student(id=3, name="Jim", grade=75),
]

#create a route to get all students

@app.get("/students/")


#read all students
def read_students():
    return students


@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student


@app.put("/students/{student_id}")
def update_student(student_id: int, Updated_Student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = Updated_Student
            return Updated_Student
    return {"error": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return deleted_student
    return {"error": "Student not found"}