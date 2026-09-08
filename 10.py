from typing import Optional, Union


def get_discounted_price_old(price: float, discount: Optional[float] = None) -> float:
    if discount is not None:
        return price - discount
    return price

def get_discounted_price(price: float, discount: float | None = None)-> float:
    if discount is not None:
        return price -(price * discount)

    return price

print(get_discounted_price(100.0,0.2))
print(get_discounted_price(100.0))