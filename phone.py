from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, refurbished_phones = 0):
        super().__init__(
            name, price, quantity
        )

        # Check validity of assigned arguments
        assert refurbished_phones >= 0, "No. of refurbised phones must be greater than or equal to 0."

        # Assign properties to self 
        self.refurbished_phones = refurbished_phones
