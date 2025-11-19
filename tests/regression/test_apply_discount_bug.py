def test_apply_discount_regression():
    from src.pricing import apply_discount
    assert apply_discount(100.0, 10) == 90.0
