import random

import items
import monsters
import player
import world


def fight(name):
    enemy_health = monsters.monsters[name]
    print(f"A {name} attacks!")

    while enemy_health > 0 and player.health > 0:
        enemy_health -= items.items["Sword"]
        if enemy_health > 0:
            hit = random.randint(1, 5)
            player.health = max(0, player.health - hit)
            print(f"You hit it. It hits you for {hit}. Health: {player.health}")

    if player.health > 0:
        print(f"You defeated the {name}!")
        return True
    print("You were defeated!")
    return False


room = "Start"
quest = False
complete = False
defeated = 0
directions = {"w": "north", "s": "south", "a": "west", "d": "east"}

print("Find the Crystal, return it to N, then defeat the Dragon at B!")

while player.health > 0:
    world.show_map(room)
    print(f"Health: {player.health}/{player.max_health} | Monsters: {defeated}/3")
    print("WASD move | E interact/fight | I inventory | P potion | Q quit")
    command = input("Command: ").lower()

    if command == "q":
        break
    elif command in directions:
        next_room = world.move(room, directions[command])
        if next_room:
            room = next_room
        else:
            print("You cannot go that way.")
    elif command == "i":
        player.show_inventory()
    elif command == "p":
        player.use_potion()
    elif command == "e":
        if room == "Village":
            if not quest:
                quest = input("NPC: Will you help? (y/n): ").lower() == "y"
                if quest:
                    print("Defeat 3 monsters and bring the Crystal back here!")
            elif defeated == 3 and not complete:
                complete = True
                print("Quest complete! Find the Dragon at B.")
            elif complete:
                print("The kingdom thanks you. Find the Dragon at B!")
            else:
                print(f"Defeat {3 - defeated} more monsters.")
        elif room == "Dragon's Lair":
            if complete and fight("Dragon"):
                print("You saved the kingdom. YOU WIN!")
                break
            elif not complete:
                print("Complete the quest first.")
        elif quest and not complete:
            enemy = random.choice(list(monsters.monsters)[:5])
            if fight(enemy):
                defeated += 1
                loot = random.choice(["Potion", "Armor", "Gold"])
                if loot == "Armor" and "Armor" not in player.inventory:
                    player.inventory.append("Armor")
                    player.max_health += items.items["Armor"]
                    player.health += items.items["Armor"]
                    print("Armor found! +25 health.")
                else:
                    player.inventory.append(loot)
                    print(f"You found {loot}!")
                if defeated == 3:
                    player.inventory.append("Crystal")
                    print("You found the Crystal!")
        else:
            print("Accept the quest from N first.")
    elif command not in ("w", "a", "s", "d"):
        print("Invalid command.")

if player.health <= 0:
    print("GAME OVER!")
elif command == "q":
    print("You left the game.")
