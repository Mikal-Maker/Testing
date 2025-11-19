import pytest
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

@pytest.mark.parametrize(
	"text,expected",
	[
		("$1,234.50", 1234.50),
		("12.5", 12.5),
		("$0.99", 0.99),
	],
)
def test_parse_price_valid(text, expected):
	assert parse_price(text) == expected

@pytest.mark.parametrize(
	"text",
	["", "abc", "$12,34,56"],
)
def test_parse_price_invalid(text):
	with pytest.raises(ValueError):
		parse_price(text)

@pytest.mark.parametrize(
	"value,expected",
	[
		(123.4567, "$123.46"),
		(0, "$0.00"),
		(1.5, "$1.50"),
	],
)
def test_format_currency(value, expected):
	assert format_currency(value) == expected

@pytest.mark.parametrize(
	"price,percent,expected",
	[
		(100.00, 0, 100.00),
		(100.00, 50, 50.00),
		(800.00, 10, 720.00),
		(1000.00, 99, 10.00),
		(1.00, 200, -1.00),
	],
)
def test_apply_discount_valid(price, percent, expected):
	assert apply_discount(price, percent) == expected

@pytest.mark.parametrize(
	"price,percent",
	[
		(100.00, -10),
		(100.00, -0.1)
	],
)
def test_apply_discount_invalid(price, percent):
	with pytest.raises(ValueError):
		apply_discount(price,percent)

@pytest.mark.parametrize(
	"price,rate,expected",
	[
		(100.00, 0.1, 110.00),
		(25.00, 0, 25.00),
		(12.00, 1, 24.00),
	],
)
def test_add_tax_valid(price, rate, expected):
	assert add_tax(price, rate) == pytest.approx(expected)

@pytest.mark.parametrize(
	"price,rate",
	[
		(100.0, -0.07),
		(0.0, -3),
	],
)
def test_add_tax_invalid(price, rate):
	with pytest.raises(ValueError):
		add_tax(price,rate)

def test_bulk_total(prices):
	prices = [10, 20, 30, 40]
	assert bulk_total(prices, 0, 0) == 100
