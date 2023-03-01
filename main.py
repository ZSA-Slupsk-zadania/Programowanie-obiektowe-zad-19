'''Launch the game and test all its elements.'''

from game import Game
from location import Location
from character import Character
from item import Item
from monster import Monster

# Create several locations, items and monsters and add them to the "Game" class object.

location1 = Location("location1", "description1", [], [])
location2 = Location("location2", "description2", [], [])
location3 = Location("location3", "description3", [], [])

item1 = Item("item1", 1, "type1", "description1")
item2 = Item("item2", 2, "type2", "description2")
item3 = Item("item3", 3, "type3", "description3")

monster1 = Monster("monster1", 1, 1, 1, "description1")
monster2 = Monster("monster2", 2, 2, 2, "description2")
monster3 = Monster("monster3", 3, 3, 3, "description3")

location1.add_item(item1)
location2.add_item(item2)
location3.add_item(item3)

location1.add_monster(monster1)
location2.add_monster(monster2)
location3.add_monster(monster3)

game = Game(location1, Character("name", 1, 1, 1, 1, []), [])

# Test all the methods of the "Game" class.

game.move(location2)
game.fight("monster1")
game.get_item(item1)
game.save("save.txt")
game.load("save.txt")
game.display()

# Expected output:
# Location: location2
# Character: Name: name
# Age: 1
# Level: 1
# Hit Points: 1
# Gold: 1
# Equipment: []
# History: ['You were killed by monster1.']