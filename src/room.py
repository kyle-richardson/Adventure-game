
class Room:
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""
        self.items = items

    def removeItem(self, item):
        self.items.remove(item)

    def addItem(self, item):
        self.items.append(item)

    def contains(self, item):
        temp = [i.name for i in self.items[:] if i.name == item]
        return len(temp) > 0

    def __str__(self):
        return f'name: {self.name}, description: {self.desc}, items: {self.items}'
