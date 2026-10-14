"""Unconditional repair acceptance check for a disposable sample workspace."""
from sample_service.pricing import calculate_total

actual=calculate_total([{'price':25,'quantity':4}],discount_percent=10)
if actual != 90:
    raise SystemExit('Discount regression persists: expected 90')
print('Discount regression resolved')
