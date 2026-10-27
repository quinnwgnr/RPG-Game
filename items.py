class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Items:
    def __init__(self):
        self.items = [
            Item("Sword", 5),
            Item("Potion", 20),
            Item("Armor", 25),
            Item("Gold", 10),
            Item("Crystal", 0),
        ]

    def value(self, name):
        for item in self.items:
            if item.name == name:
                return item.value
        return 0
