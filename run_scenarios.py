from cargar_csv import load_fixture
from decimal import Decimal

def run():
    print("Ejecutando escenarios E01-E15...")
    orders = load_fixture()
    
    # E01
    o1 = orders["O001"]
    print(f"E01 0001: total {o1.total.amount:.2f} | 10% = {o1.total.amount * Decimal('0.1'):.2f} | final {o1.total.amount * Decimal('0.9'):.2f}")
    
    # E02
    o2 = orders["O002"]
    print(f"E02 0002: total {o2.total.amount:.2f} | 0% = 0.00 | final {o2.total.amount:.2f}")

    # E03
    o3 = orders["O003"]
    try:
        o3.confirm()
    except Exception as e:
        print(f"E03 0003 confirmar: {type(e).__name__}: {e} ('{o3.status.value}', {[ev.name for ev in o3.events]})")

    # E04
    o5 = orders["O005"]
    print(f"E04 0005: total {o5.total.amount:.2f} | 0% = 0.00 | final {o5.total.amount:.2f}")

    # E05
    o6 = orders["O006"]
    print(f"E05 0006: total {o6.total.amount:.2f} | 5% = {o6.total.amount * Decimal('0.05'):.2f} | final {o6.total.amount * Decimal('0.95'):.2f}")

    # E06
    o7 = orders["O007"]
    try:
        o7.confirm()
    except Exception as e:
        print(f"E06 0007 confirmar: {type(e).__name__}: {e} ('{o7.status.value}', {[ev.name for ev in o7.events]})")

    # E07
    o8 = orders["O008"]
    o8.confirm()
    print(f"E07 0008 confirmar: OK ('{o8.status.value}', {[ev.name for ev in o8.events]})")

    # E08
    o9 = orders["O009"]
    from app.domain import OrderItem, Money
    try:
        o9.add_item(OrderItem(sku="SKU003", quantity=2, unit_price=Money(Decimal("120.00"))))
    except Exception as e:
        print(f"E08 0009 +SKU003x2: {type(e).__name__}: {e} | unidades: {o9.units} ('{o9.status.value}', {[ev.name for ev in o9.events]})")

    # E09
    o10 = orders["O010"]
    print(f"E09 0010: total {o10.total.amount:.2f} | 0% = 0.00 | final {o10.total.amount:.2f}")

    # E10
    o11 = orders["O011"]
    print(f"E10 0011: total {o11.total.amount:.2f} | 0% = 0.00 | final {o11.total.amount:.2f}")

    # E11
    o12 = orders["O012"]
    o12.confirm()
    try:
        o12.ship("")
    except Exception as e:
        print(f"E11 0012 confirmar: OK | enviar sin guia: {type(e).__name__}: {e} ('{o12.status.value}', {[ev.name for ev in o12.events]})")

    # E12
    o13 = orders["O013"]
    o13.confirm()
    try:
        o13.confirm()
    except Exception as e:
        print(f"E12 0013 la confirmacion: OK | 2a: {type(e).__name__}: {e} ('{o13.status.value}', {[ev.name for ev in o13.events]})")

    # E13
    o14 = orders["O014"]
    o14.confirm()
    o14.ship("GUIA123")
    try:
        o14.cancel("Motivo")
    except Exception as e:
        print(f"E13 0014 cancelar: {type(e).__name__}: {e} ('{o14.status.value}', {[ev.name for ev in o14.events]})")

    # E14
    o15 = orders["O015"]
    o15.confirm()
    o15.ship("GUIA123")
    o15.return_order()
    print(f"E14 0015 devolver: OK ('{o15.status.value}', {[ev.name for ev in o15.events]})")

    # E15
    o16 = orders["O016"]
    o16.confirm()
    o16.ship("GUIA123")
    o16.deliver()
    print(f"E15 0016 entregar: OK ('{o16.status.value}', {[ev.name for ev in o16.events]})")

if __name__ == "__main__":
    run()
