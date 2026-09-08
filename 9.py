from dataclasses import dataclass

@dataclass

class Product:
    name: int
    price: float
    quantity: int = 0


item1 = Product(name = "Laptop", price = 9999.99, quantity = 6)

item2 = Product(name = "Laptop", price = 9999.99, quantity = 6)


print(item1)

ans = (item1 == item2)

print(ans)


class OldProduct:
    def __init__(self,name:str,price:float,quantity:int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name = {self.name!r}, price = {self.price!r}, quantity = {self.quantity!r})"

    def __eq__(self, other):
        if not isinstance(other, OldProduct):
            return NotImplemented

        return(self.name, self.price,self.quantity) == (other.name,other.price,other.quantity)