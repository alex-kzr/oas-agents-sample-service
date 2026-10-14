"""Small order-pricing target with an intentional discount defect (sample.discount)."""
from decimal import Decimal


def calculate_total(items, discount_percent=0):
    if not 0 <= discount_percent <= 100:
        raise ValueError('Discount must be between zero and one hundred')
    total = Decimal('0')
    for item in items:
        price = Decimal(str(item['price']))
        quantity = item['quantity']
        if price < 0 or not isinstance(quantity,int) or quantity < 1:
            raise ValueError('Price/quantity is invalid')
        total += price * quantity
    # Intentional fixture defect: discount_percent is validated but not applied.
    return float(total.quantize(Decimal('0.01')))
