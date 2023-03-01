'''
The "Item" class containing information about the name, price, type (e.g. weapon, armor, potion) and description of the item. Implement a method that allows you to display information about the item.
'''
import json

class Item:

    def __init__(self, name, price, type, description):
        self.name = name
        self.price = price
        self.type = type
        self.description = description

    def display(self):
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Type: " + self.type)
        print("Description: " + self.description)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)