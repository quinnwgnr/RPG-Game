rooms = {
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


def show_map(room):
    print("\nMAP: Start -- Trail -- Village (N) -- Clearing -- Forest -- Ruins -- Lair (B)")
    print("               |                    |")
    print("             Woods -- Lake ---------")
    print(f"You are in: {room} (*)")
    print("Exits:", ", ".join(rooms[room]) or "none")


def move(room, direction):
    return rooms[room].get(direction)
