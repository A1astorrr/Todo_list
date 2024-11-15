from fastapi import FastAPI
from app.todo.router import router as todo_router

app = FastAPI()

app.include_router(todo_router)

@app.get("/",
         tags=["Приветствие"])
def welcome():
    return {"message": "Welcome to Todo"}

