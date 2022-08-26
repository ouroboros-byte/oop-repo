class Item:
    def __init__(self, name: str, price: float, quantity: int = 0):
        
        # Check validity of assigned arguments
        assert price >= 0, "Price input must be more than 0."
        assert quantity >= 0, "Quantity input must be more than 0."

        # Assign properties to self
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Instance created: {name}")

    def liquid_asset_value(self):
        return self.price * self.quantity

item1 = Item("Phone", 500, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.liquid_asset_value())
print(item2.liquid_asset_value())