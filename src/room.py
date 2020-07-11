# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""
        self.items = items

    def __str__(self):
        return f'name: {self.name}, description: {self.desc}, items: {self.items}'
