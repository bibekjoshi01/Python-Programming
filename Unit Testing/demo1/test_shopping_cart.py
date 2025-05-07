import pytest
from shopping_cart import ShoppingCart
from item_db import ItemDB
from unittest.mock import Mock


@pytest.fixture
def cart():
    return ShoppingCart(max_size=5)


def test_can_add_item_to_cart(cart):
    cart.add_item("apple")
    assert cart.get_size() == 1


def test_when_item_added_cart_has_item(cart):
    cart.add_item("banana")
    assert "banana" in cart.get_items()


def test_when_add_more_than_max_size_should_fail(cart):
    for i in range(5):
        cart.add_item(f"item{i}")

    with pytest.raises(OverflowError):
        cart.add_item(f"item{i}")


def test_can_get_total_price(cart):
    cart.add_item("apple")
    cart.add_item("banana")

    def mock_get_item(item: str) -> float:
        if item == "apple":
            return 1.0
        if item == "banana":
            return 2.0

    item_db = ItemDB()
    item_db.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_db) == 3.0
