'''
The "Game" class containing information about the current location of the player, his character and the history of the game. Implement methods that allow you to move to another location, fight the monster, obtain items and save/load the game from a file.
Create several locations, items and monsters and add them to the "Game" class object.
'''
import json

class Game:

    def __init__(self, location, character, history):
        self.location = location
        self.character = character
        self.history = history

    def move(self, location):
        self.location = location

    def fight(self, monsterName):
        for monster in self.location.monsters:
            if monster.name == monsterName:
                break
        self.character.change_hp(-monster.level)
        monster.change_hp(-self.character.level)
        if monster.hp <= 0:
            self.location.remove_monster(monster)
            self.character.change_exp(1)
            self.character.gold += monster.gold
            self.history.append("You killed " + monster.name + " and gained " + str(monster.gold) + " gold.")
        else:
            self.history.append("You were killed by " + monster.name + ".")

    def get_item(self, item):
        self.character.add_item(item)
        self.location.remove_item(item)
        self.history.append("You got " + item.name + ".")

    # Savefiles use JSON format
    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.toJSON())

    def load(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.location = data["location"]
            self.character = data["character"]
            self.history = data["history"]

    def display(self):
        print("Location: " + str(self.location))
        print("Character: " + str(self.character))
        print("History: " + str(self.history))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)