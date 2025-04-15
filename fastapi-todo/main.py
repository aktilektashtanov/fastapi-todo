from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Модель задачи
class Task(BaseModel):
    id: int
    title: str
    is_done: bool = False

# Хранилище задач (в памяти)
tasks: List[Task] = []

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def mark_done(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.is_done = True
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted"}