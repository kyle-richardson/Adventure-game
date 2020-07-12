from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["brick", "torch"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["map", "pencil"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["twig", "rock"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south.""", ["treasure", "bag"]),
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

# Make a new player object that is currently in the 'outside' room.
print("******START GAME*******")

name = input("What is your name, adventurer? ")
player = Player(name, room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"Hi {player.name}. Good luck!")

while ("bag" not in player.items):
    print("\n**********************\n")
    print(f"You are in room: {player.room.name}\n")
    print(f"{player.room.desc}\n")
    print(
        f"You look around and see the following items in the room: {player.room.items}\n")
    print(f"You are holding the following items: {player.items}\n")
    print("**********************\n")
    x = input(
        "Enter N,S,E, or W to attempt to move to another room, or interact with items with 'get [item]' or 'drop [item]' commands (q to quit the game): ")
    print("\n")
    lowerCase = str(x).lower()
    if lowerCase == "q":
        print("You suddenly fall down, unconscious.  Then you slowly disappear. Farewell, stranger.")
        sys.exit("*****END GAME*****")
    elif lowerCase == "n" or lowerCase == "s" or lowerCase == "e" or lowerCase == "w":
        y = f'{lowerCase}_to'
        print(f"Starting to move {x}...")
        if getattr(player.room, y):
            player.moveRoom(getattr(player.room, y))
            print(f'{player.name} moved to room: {player.room.name}')
        else:
            print("You hit a wall.  Try another direction.")
    elif lowerCase.split(" ")[0] == "get" and len(lowerCase.split(" ")) > 1:
        itemName = lowerCase.split(" ")[1]
        if itemName:
            if itemName in player.room.items:
                player.pickupItem(itemName)
                print(f'{player.name} picked up {itemName}')
                if itemName == 'treasure':
                    print("You dust off the treasure chest, and find ancient engravings.  Your heart races as you slowly open the chest... Suddenly, your vision blacks out, and you writhe in pain on the floor for what seems like hours before it finally subsides.  You look around and wipe your face only to realize that the treasure chest was booby trapped with a poison gas! Good thing you are still alive.  Well, it seems like this quest for treasure was a hoax.")
            else:
                print(f"{itemName} is not found in this room. Try again.")
        else:
            print("Invalid input. Correct input is 'get [item]'. Try again.")
    elif lowerCase.split(" ")[0] == "drop" and len(lowerCase.split(" ")) > 1:
        itemName = lowerCase.split(" ")[1]
        if itemName:
            if itemName in player.items:
                player.dropItem(itemName)
                print(f'{player.name} dropped up {itemName}')
            else:
                print(f"You are not holding {itemName}. Try again.")
        else:
            print("Invalid input. Correct input is 'drop [item]'. Try again.")
    else:
        print("Invalid input.  Try again.")

print(
    f"You open the small bag and find a marvelous diamond.  This looks like it is worth a fortune! Good work, {player.name}. Now, don't forget to come back and tip me when you're all rich and stuff. I mean, I did help you quite a bit. ... pretty please?")
print("*****END GAME*****")
