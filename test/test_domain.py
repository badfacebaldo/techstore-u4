import pytest
from decimal import Decimal
from app.domain import Money, InvalidOrderData, InvalidOrderTransition
from cargar_csv import load_fixture

def test_money_monto_negativo():
    with pytest.raises(InvalidOrderData):
        Money(Decimal("-10.00"))

def test_pedido_o001_inicial_draft():
    orders = load_fixture()
    order = orders["O001"]
    assert order.status.value == "DRAFT"
    assert order.units == 4
    assert order.total.amount == Decimal("2100.00")

def test_confirmar_pedido_valido():
    orders = load_fixture()
    order = orders["O001"]
    order.confirm()
    assert order.status.value == "CONFIRMED"
    assert len(order.events) == 1
    assert order.events[0].name == "OrderConfirmed"

def test_confirmar_dos_veces_lanza_excepcion():
    orders = load_fixture()
    order = orders["O001"]
    order.confirm()
    with pytest.raises(InvalidOrderTransition):
        order.confirm()