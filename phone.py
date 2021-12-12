from item import Item
class Phone(Item):
    all = []
    ## Phone class inherits from Item
    def __init__(self, name: str = "Phone", price: float = 100, quantity: int = 5,broken_phones: int=0):
        super().__init__(name=name, price=price, quantity=quantity)
        ### Super allow us to access all the parent attributes
        assert broken_phones>=0, f"Broken phones {broken_phones} is not greater or equal to 0"
        self.broken_phones = broken_phones
        Phone.all.append(self)
    def __repr__(self):
        # return str(self.__dict__)
        ## best practice to understand how show what have been created
        return f"('{self.name}','{self.price}',{self.quantity}','{self.broken_phones}')"
