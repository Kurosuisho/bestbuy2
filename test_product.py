import pytest
from products import Product


def test_create_normal_product():
    # Testing addition of a product
    product = Product("Test Product", price=100.0, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.get_quantity() == 10
    assert product.is_active()


def test_create_invalid_product():
    # Test invalid product addition with empty name
    with pytest.raises(ValueError, match="Product name cannot be empty."):
        Product("", price=1450, quantity=100)

    # Test invalid product addition with negative price
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    # Test invalid product addition with negative quantity
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_becomes_inactive_when_quantity_zero():
    # Test product deactivation when quantity becomes zero
    product = Product("Test Product", price=100.0, quantity=10)
    product.set_quantity(0)
    assert product.get_quantity() == 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    # Test purchasing a product
    product = Product("Test Product", price=50.0, quantity=10)
    total_price = product.buy(2)
    assert total_price == 100.0  # 2 * 50
    assert product.get_quantity() == 8


def test_purchase_more_than_available_quantity_raises_exception():
    # Test purchasing more products than available stock
    product = Product("Test Product", price=50.0, quantity=5)
    with pytest.raises(ValueError, match="Not enough quantity in stock."):
        product.buy(10)
