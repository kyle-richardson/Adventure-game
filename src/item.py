class Item:
    def __init__(self, name, desc=""):
        self.name = name
        self.desc = desc

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
