# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI(title="API de Tareas")

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

# "Base de datos" en memoria
db: Dict[int, Task] = {}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(db.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    if task.id in db:
        raise HTTPException(status_code=400, detail="ID ya existe")
    db[task.id] = task
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if task_id != updated_task.id:
        raise HTTPException(status_code=400, detail="IDs no coinciden")
    db[task_id] = updated_task
    return updated_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del db[task_id]
    return


def main():
        uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
if __name__ == "__main__":
    main()