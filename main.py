import random

import items
import monsters
import player
import world


class Game:
    def __init__(self):
        self.player = player.Player()
        self.items = items.Items()
        self.monsters = monsters.Monsters()
        self.world = world.World()
        self.room = "Start"
        self.quest = False
        self.complete = False
        self.defeated = 0
        self.won = False

    def run(self):
        print("Find the Crystal, return it to N, then defeat the Dragon!")

        while self.player.health > 0 and not self.won:
            self.world.show_map(self.room)
            print("Health: " + str(self.player.health) + "/" +
                  str(self.player.max_health) + " | Monsters: " +
                  str(self.defeated) + "/3")

            if not self.quest:
                print("Task: Find N and accept the quest.")
            elif not self.complete:
                print("Task: Defeat 3 monsters and bring the Crystal to N.")
            else:
                print("Task: Find B and defeat the Dragon.")

            print("WASD move | E interact/fight | I inventory | P potion | Q quit")
            command = input("Command: ").lower()

            if command == "q":
                break
            elif command in ["w", "a", "s", "d"]:
                self.move(command)
            elif command == "i":
                self.player.show_inventory()
            elif command == "p":
                self.player.use_potion()
            elif command == "e":
                self.interact()
            else:
                print("Invalid command.")

        if self.won:
            print("You saved the kingdom. YOU WIN!")
        elif self.player.health <= 0:
            print("GAME OVER!")
        else:
            print("You left the game.")

    def move(self, command):
        directions = {"w": "north", "a": "west", "s": "south", "d": "east"}
        next_room = self.world.move(self.room, directions[command])

        if next_room:
            self.room = next_room
        else:
            print("You cannot go that way.")

    def interact(self):
        if self.room == "Village":
            self.talk_to_npc()
        elif self.room == "Dragon's Lair":
            if self.complete:
                self.won = self.fight(self.monsters.dragon)
            else:
                print("Complete the quest before facing the Dragon.")
        elif self.quest and not self.complete:
            self.fight(self.monsters.random_monster())
        else:
            print("Find N and accept the quest first.")

    def talk_to_npc(self):
        if not self.quest:
            self.quest = input("NPC: Will you help? (y/n): ").lower() == "y"
            if self.quest:
                print("Defeat 3 monsters and bring back the Crystal!")
        elif self.defeated == 3:
            self.complete = True
            print("Quest complete! Find the Dragon at B.")
        else:
            print("Defeat " + str(3 - self.defeated) + " more monsters.")

    def fight(self, monster):
        print("A " + monster.name + " attacks!")

        while monster.health > 0 and self.player.health > 0:
            monster.health -= self.items.value("Sword")

            if monster.health > 0:
                hit = random.randint(1, 5)
                self.player.health = max(0, self.player.health - hit)
                print("You hit it. It hits you for " + str(hit) +
                      ". Health: " + str(self.player.health))

        if self.player.health == 0:
            print("You were defeated!")
            return False

        print("You defeated the " + monster.name + "!")
        if monster.name == "Dragon":
            return True

        self.defeated += 1
        self.collect_item()
        return False

    def collect_item(self):
        reward = random.choice(["Potion", "Armor", "Gold"])

        if reward == "Armor" and "Armor" not in self.player.inventory:
            self.player.inventory.append("Armor")
            self.player.max_health += self.items.value("Armor")
            self.player.health += self.items.value("Armor")
            print("You found Armor! +25 health.")
        else:
            self.player.inventory.append(reward)
            print("You found " + reward + "!")

        if self.defeated == 3:
            self.player.inventory.append("Crystal")
            print("You found the Crystal!")


if __name__ == "__main__":
    Game().run()
