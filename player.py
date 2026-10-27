
max_health = 100
health = max_health
inventory = ["Sword", "Potion"]

def show_inventory():
    print("Inventory:", inventory)

def use_potion():
    global health

    if "Potion" not in inventory:
        print("You have no potions!")
        return False
    if health == max_health:
        print("Your health is already full.")
        return False

    health = min(max_health, health + 20)
    inventory.remove("Potion")
    print("You used a potion! Health:", health)
    return True
