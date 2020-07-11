# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def moveRoom(self, room):
        self.room = room

    def pickupItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        return f'name:{self.name}, current room: {self.room}, items: {self.items}'
