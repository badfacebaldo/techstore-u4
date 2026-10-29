from fastapi import FastAPI, HTTPException
from cargar_csv import load_fixture
from app.domain import InvalidOrderTransition, InvalidOrderData, OrderItemLimitExceeded

app = FastAPI(title="TechStore U4 API", version="1.0.0")

orders = load_fixture()

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {
        "id": order.id,
        "status": order.status.value,
        "units": order.units,
        "total": str(order.total.amount)
    }

@app.post("/orders/{order_id}/confirm")
def confirm_order(order_id: str):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    try:
        order.confirm()
    except InvalidOrderTransition as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    except (InvalidOrderData, OrderItemLimitExceeded) as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {
        "id": order.id,
        "status": order.status.value,
        "events": [e.name for e in order.events]
    }

@app.post("/orders/{order_id}/ship")
def ship_order(order_id: str, tracking_number: str):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    try:
        order.ship(tracking_number)
    except InvalidOrderTransition as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    except InvalidOrderData as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {
        "id": order.id,
        "status": order.status.value
    }