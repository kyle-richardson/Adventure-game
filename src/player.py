# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def moveRoom(self, room):
        self.room = room
        print(f'{self.name} moved to room: {room.name}')

    def pickupItem(self, item):
        self.items.append(item)
        print(f'{self.name} picked up {item}')

    def dropItem(self, item):
        self.items.remove(item)
        print(f'{self.name} dropped {item}')

    def contains(self, item):
        temp = [i.name for i in self.items[:] if i.name == item]
        return len(temp) > 0

    def __str__(self):
        return f'name:{self.name}, current room: {self.room}, items: {self.items}'
