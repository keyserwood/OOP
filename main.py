import pandas as pd
class Item:
    ### Global attribute for all the class -- inherintance
    pay_rate = 0.8 # Pay rate after 20% discount
    all = [] # List of items
    def __init__(self,name: str="Phone",price: float=100,quantity: int=5):
        ### Run validation to the received args 
        assert price>= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >=0
        
        ### Constructor -- magic methods
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def __str__(self):
        ### Str method to print an instance
        print("name:",self.name)
        print("price:",self.price)
        print('quantity:',self.quantity)
        return """"""

    def __repr__(self):
        # return str(self.__dict__)
        ## best practice to understand how show what have been created
        return f"Item('{self.name}','{self.price}',{self.quantity}')"

    def calculate_total_price(self):
        return self.quantity*self.price
    def apply_discount(self):
        """Apply discount with discount rate for the attribute"""
        self.price = self.price*self.pay_rate ## Accessing pay rate linked to class
        ### Doing this enable also to overwrite pay rate for a specific instance
    @classmethod
    def instantiate_from_csv(cls):
        df = pd.read_csv("item.csv")
        for i in range(len(df)):
            name = df.loc[i,"name"]
            price = df.loc[i,"price"]
            quantity = df.loc[i,"quantity"]
            Item(name,price,quantity)

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
        return f"{('{self.name}','{self.price}',{self.quantity}','{self.broken_phones}')"



phone1 = Phone("jscPhonev10",500,5,0)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20",700,5,1)
print(Phone.all)






# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# Make a list of Item :
# Item.instantiate_from_csv()

# print(Item.all)



# item2.pay_rate = 0.7 ### Change the pay rate locally for item 2
# item2.apply_discount()
# print(item2.price)
# # item3 = Item(name="test",price=-1)
# ### Possible to add an arg after
# print(str(item1))
# # print(Item.__dict__) ## Print all the attributes of a class
# # print(item1.__dict__)

# item1.apply_discount() ## Apply discount to the price and overwrite the price
# print(item1.price)