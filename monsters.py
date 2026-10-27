import random


class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health


class Monsters:
    def __init__(self):
        self.names = ["Slime", "Goblin", "Wolf", "Skeleton", "Orc"]
        self.health = [15, 20, 25, 30, 35]
        self.dragon = Monster("Dragon", 60)

    def random_monster(self):
        number = random.randint(0, 4)
        return Monster(self.names[number], self.health[number])
