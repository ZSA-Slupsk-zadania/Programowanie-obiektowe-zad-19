'''
The "Location" class containing information about the name, description of the location and lists of items and monsters in the location. Implement methods to add/remove items/monsters from the location and display information about the location.
'''
import json

class Location:

    def __init__(self, name, description, items, monsters):
        self.name = name
        self.description = description
        self.items = items
        self.monsters = monsters

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, itemName):
        for item in self.items:
            if item.name == itemName:
                self.items.remove(item)

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monsterName):
        for monster in self.monsters:
            if monster.name == monsterName:
                self.monsters.remove(monster)

    def display(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Items: " + str(self.items))
        print("Monsters: " + str(self.monsters))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)