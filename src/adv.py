from room import Room
from player import Player
from item import Item
import sys


# Create items

items = {
    'brick': Item("brick"),
    'torch': Item("torch"),
    'mapp': Item("map"),
    'shield': Item("shield"),
    'twig': Item("twig"),
    'rock': Item("rock"),
    'sword': Item("sword"),
    'pencil': Item("pencil"),
    'chest': Item("chest"),
    'bag': Item("bag"),
}

brick = Item("brick")


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['brick'], items['torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['mapp'], items['shield']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['twig'], items['rock']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['sword'], items['pencil']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south.""", [items['chest'], items['bag']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

print("******START GAME*******")

name = input("What is your name, adventurer? ")
player = Player(name, room["outside"])

print(f"Hi {player.name}. Good luck!")

while (items['bag'] not in player.items):
    print("\n**********************\n")
    print(f"You are in room: {player.room.name}\n")
    print(f"{player.room.desc}\n")
    print(
        f"You look around and see the following items in the room: {player.room.items}\n")
    print(f"You are holding the following items: {player.items}\n")
    print("**********************\n")
    inp = input(
        "Enter North, South, East, West (or just the first letter) to attempt to move to another room, or interact with items with 'get [item]' ('take' and 'pickup' work as well in place of 'get') or 'drop [item]' commands (q to quit the game): ")
    print("\n")
    lowerCase = str(inp).lower()
    firstWord = lowerCase.split(" ")[0]
    if lowerCase == "q":
        print("You suddenly fall down, unconscious.  Then you slowly disappear. Farewell, stranger.")
        sys.exit("*****END GAME*****")
    elif lowerCase in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
        direction = f'{lowerCase[0]}_to'
        print(f"Starting to move {inp}...")
        if getattr(player.room, direction):
            player.moveRoom(getattr(player.room, direction))
        else:
            print("You hit a wall.  Try another direction.")
    elif firstWord in ["get", "pickup", "take"]:
        if len(lowerCase.split(" ")) > 1:
            itemName = lowerCase.split(" ")[1]
            if player.room.contains(itemName):
                player.pickupItem(items[itemName])
                player.room.removeItem(items[itemName])
                if itemName == 'chest':
                    print("You dust off the treasure chest, and find ancient engravings.  Your heart races as you slowly open the chest... Suddenly, your vision blacks out, and you writhe in pain on the floor for what seems like hours before it finally subsides.  You look around and wipe your face only to realize that the treasure chest was booby trapped with a poison gas! Good thing you are still alive.  Well, it seems like this quest for treasure was a hoax.")
            else:
                print(f"{itemName} is not found in this room. Try again.")
        else:
            print(
                f"Invalid input. Correct format is '{firstWord} [item]'. Try again.")
    elif firstWord == "drop":
        if len(lowerCase.split(" ")) > 1:
            itemName = lowerCase.split(" ")[1]
            if player.contains(itemName):
                player.dropItem(items[itemName])
                player.room.addItem(items[itemName])
            else:
                print(f"You are not holding {itemName}. Try again.")
        else:
            print("Invalid input. Correct format is 'drop [item]'. Try again.")
    else:
        print("Invalid input.  Try again.")

print(
    f"You open the small bag and find a marvelous diamond.  This looks like it is worth a fortune! Good work, {player.name}. Now, don't forget to come back and tip me when you're all rich and stuff. I mean, I did help you quite a bit. ... pretty please?")
print("*****END GAME*****")
