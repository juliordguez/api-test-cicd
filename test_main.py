# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_task():
    # Aseguramos base "limpia" creando con un ID nuevo
    payload = {"id": 1, "title": "Primera tarea", "done": False}
    response = client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Primera tarea"
    assert data["done"] is False


def test_list_tasks():
    # Ya debe existir al menos la tarea con id 1
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(task["id"] == 1 for task in data)


def test_get_task_ok():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Primera tarea"


def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Tarea no encontrada"


def test_update_task_ok():
    payload = {"id": 1, "title": "Tarea actualizada", "done": True}
    response = client.put("/tasks/1", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarea actualizada"
    assert data["done"] is True


def test_delete_task_ok():
    response = client.delete("/tasks/1")
    assert response.status_code == 204

    # Confirmar que ya no existe
    response = client.get("/tasks/1")
    assert response.status_code == 404
