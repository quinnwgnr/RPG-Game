class Player:
    def __init__(self):
        self.max_health = 100
        self.health = 100
        self.inventory = ["Sword", "Potion"]

    def show_inventory(self):
        print("Inventory: " + str(self.inventory))

    def use_potion(self):
        if "Potion" in self.inventory and self.health < self.max_health:
            self.health = self.health + 20
            if self.health > self.max_health:
                self.health = self.max_health
            self.inventory.remove("Potion")
            print("You used a potion. Health: " + str(self.health))
        else:
            print("No potion available or health is already full.")
