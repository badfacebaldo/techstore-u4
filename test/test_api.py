import pytest
from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_1_confirm_o013_exitoso():
    # 1) POST /orders/O013/confirm: 200, con status CONFIRMED y el evento OrderConfirmed.
    response = client.post("/orders/O013/confirm")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "CONFIRMED"
    assert "OrderConfirmed" in data["events"]

def test_2_confirm_o013_segunda_vez_conflict():
    # 2) El mismo POST una segunda vez: 409 Conflict, sin cambios en el pedido.
    # (O013 ya fue confirmado en el test anterior)
    response = client.post("/orders/O013/confirm")
    assert response.status_code == 409

def test_3_get_orden_inexistente_404():
    # 3) GET /orders/O999: 404 Not Found.
    response = client.get("/orders/O999")
    assert response.status_code == 404

def test_4_confirm_o007_sin_articulos_422():
    # 4) POST /orders/O007/confirm: 422, porque el pedido no tiene artículos.
    response = client.post("/orders/O007/confirm")
    assert response.status_code == 422