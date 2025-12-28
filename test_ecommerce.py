import pytest
from product_logic import login, place_zara_coat_only, shipping_and_place_order
from orderid import verify_and_print_order_summary

@pytest.mark.parametrize("email, password", [
    ("phanikumarperapa@gmail.com", "Phani119$"),
    ("phanikumarperapa@gmail.com", "Phani119$"),
    ("phanikumarperapa@gmail.com", "Phani119$")
])
def test_positive_purchase_flow(driver, wait, email, password):
    """Positive Flow: Login, Add to Cart, Place Order, and ID Verification."""
    login(driver, wait, email, password)
    place_zara_coat_only(driver, wait)
    shipping_and_place_order(driver, wait)
    verify_and_print_order_summary(driver, wait)

@pytest.mark.parametrize("email, password, expected_error", [
    ("invalid_user@gmail.com", "Phani119$", "Incorrect email or password."),
    ("phanikumarperapa@gmail.com", "WrongPass123", "Incorrect email or password.")
])
def test_negative_login_scenarios(driver, wait, email, password, expected_error):
    """Negative Flow: Verification of error toast for invalid credentials."""
    actual_error = login(driver, wait, email, password, expected_status="fail")
    assert expected_error in actual_error