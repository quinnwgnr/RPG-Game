class World:
    def __init__(self):
        self.rooms = {
            "Start": {"east": "Trail"},
            "Trail": {"west": "Start", "east": "Village", "south": "Woods"},
            "Village": {"west": "Trail", "east": "Clearing"},
            "Woods": {"north": "Trail", "east": "Lake"},
            "Lake": {"west": "Woods", "north": "Clearing"},
            "Clearing": {"west": "Village", "east": "Forest", "south": "Lake"},
            "Forest": {"west": "Clearing", "east": "Ruins"},
            "Ruins": {"west": "Forest", "east": "Dragon's Lair"},
            "Dragon's Lair": {"west": "Ruins"},
        }

    def show_map(self, room):
        print("\nStart -- Trail -- Village (N) -- Clearing -- Forest -- Ruins -- Lair (B)")
        print("               |                    |")
        print("             Woods -- Lake ---------")
        print("You are in: " + room)
        print("Exits: " + ", ".join(self.rooms[room]))

    def move(self, room, direction):
        return self.rooms[room].get(direction)
