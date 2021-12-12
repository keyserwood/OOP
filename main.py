from item import Item

Item.instantiate_from_csv()

# print(Item.all)
item1 = Item("test",110)
print(item1.name)

## Setting an attribute
item1.name="TEst"
## Getting an attribute
print(item1.name)

# phone1 = Phone("jscPhonev10",500,5,0)
# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20",700,5,1)
# print(Phone.all)






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