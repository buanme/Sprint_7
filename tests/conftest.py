import pytest

from methods.courier import Courier
from methods.orders import Orders


@pytest.fixture
def courier():
    new_courier = Courier()
    return new_courier


@pytest.fixture
def order():
    new_order = Orders()
    return new_order
