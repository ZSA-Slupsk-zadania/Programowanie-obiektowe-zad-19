'''
The "Character" class containing information about the character's name, age, experience level, hit points, gold and equipment. Implement methods to add/remove items from inventory, change experience level and hitpoints, and display character information.
'''

import json

class Character:

    def __init__(self, name, age, level, hp, gold, equipment):
        self.name = name
        self.age = age
        self.level = level
        self.hp = hp
        self.gold = gold
        self.equipment = equipment

    def add_item(self, item):
        self.equipment.append(item)

    def remove_item(self, item):
        self.equipment.remove(item)

    def change_exp(self, exp):
        self.level += exp

    def change_hp(self, hp):
        self.hp += hp

    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Level: " + str(self.level))
        print("Hit Points: " + str(self.hp))
        print("Gold: " + str(self.gold))
        print("Equipment: " + str(self.equipment))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)