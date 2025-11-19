import pytest
from src.pricing import bulk_total
from src.order_io import load_order, write_receipt

def test_load_order_integration(tmp_path):
	input_file = tmp_path / "order.csv"
	input_file.write_text("thing,$10.00\nstuff,5.50\n", encoding="utf-8")

	items = load_order(input_file)
	prices = [item[1] for item in items]
	discount_percent = 10
	tax_rate = 0.1
	total = bulk_total(prices, discount_percent, tax_rate)

	write_receipt(tmp_path / "receipt.txt", items, discount_percent, tax_rate)
	output_txt = (tmp_path / "receipt.txt").read_text(encoding="utf-8")

	assert "thing: $10.00" in output_txt
	assert "stuff: $5.50" in output_txt
	assert "TOTAL:" in output_txt
