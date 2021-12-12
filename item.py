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
        self.__name = name ## Double __ makes the value private
        self.__price = price
        self.quantity = quantity
        Item.all.append(self)


    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value < 0 :
            raise Exception("Price should be positive")
        else:
            self.__price=value
        

    @property
    # Property decorator = Read only attribute 
    def name(self):
        return self.__name

    @name.setter ## Setter for a value
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long")
        else:
            self.__name=value
    def __str__(self):
        ### Str method to print an instance
        print("name:",self.name)
        print("price:",self.__price)
        print('quantity:',self.quantity)
        return """"""

    def __repr__(self):
        # return str(self.__dict__)
        ## best practice to understand how show what have been created
        return f"Item('{self.name}','{self.__price}',{self.quantity}')"

    def calculate_total_price(self):
        return self.quantity*self.__price
    def apply_discount(self):
        """Apply discount with discount rate for the attribute"""
        self.__price = self.__price*self.pay_rate ## Accessing pay rate linked to class
        ### Doing this enable also to overwrite pay rate for a specific instance
    @classmethod
    def instantiate_from_csv(cls):
        df = pd.read_csv("item.csv")
        for i in range(len(df)):
            name = df.loc[i,"name"]
            price = df.loc[i,"price"]
            quantity = df.loc[i,"quantity"]
            Item(name,price,quantity)
