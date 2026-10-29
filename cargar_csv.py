import csv
from pathlib import Path
from decimal import Decimal
from app.domain import Customer, Money, OrderItem, Order

BASE_DIR = Path(__file__).resolve().parent / "datos"

def load_fixture():
    # 1. Cargar Clientes (usando utf-8-sig para evitar problemas de BOM)
    customers = {}
    with open(BASE_DIR / "clientes.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            c_id = row["cliente_id"]
            customers[c_id] = Customer(
                id=c_id,
                is_vip=row["es_vip"].strip() == "1",
                active=row["activo"].strip() == "1"
            )

    # 2. Cargar Productos
    products = {}
    with open(BASE_DIR / "productos.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row["sku"]
            products[sku] = Money(Decimal(row["precio_mxn"]))

    # 3. Cargar Pedidos (Inicialmente vacíos)
    orders = {}
    with open(BASE_DIR / "pedidos.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p_id = row["pedido_id"]
            c_id = row["cliente_id"]
            has_promo = row.get("tiene_promocion", "0").strip() == "1"
            customer = customers.get(c_id)
            if customer:
                orders[p_id] = Order(
                    id=p_id,
                    customer=customer,
                    has_promotion=has_promo
                )

    # 4. Cargar Detalles y asignarlos a cada Pedido
    with open(BASE_DIR / "detalle_pedidos.csv", mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p_id = row["pedido_id"]
            sku = row["sku"]
            qty = int(row["cantidad"])
            unit_price = products.get(sku, Money(Decimal("0.00")))
            if p_id in orders:
                item = OrderItem(sku=sku, quantity=qty, unit_price=unit_price)
                orders[p_id].add_item(item)

    return orders

if __name__ == "__main__":
    loaded_orders = load_fixture()
    print(f"--- Se cargaron exitosamente {len(loaded_orders)} pedidos ---")
    for order_id, order in loaded_orders.items():
        print(f"Pedido: {order.id} | Cliente: {order.customer.id} | Estado: {order.status.value} | Unidades: {order.units} | Total: {order.total.amount} MXN")