import csv

class Item:
    pay_rate = 0.8 # cost multiplyer with 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        # Check validity of assigned arguments
        assert price >= 0, "Price input must be more than 0."
        assert quantity >= 0, "Quantity input must be more than 0."

        # Assign properties to self 
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Instance created: {name}")

        # Actions to execute
        Item.all.append(self)

    def liquid_asset_value(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

Item.instantiate_from_csv()