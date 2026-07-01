import random


FRUIT_VALUE = 20
TRAP_PENALTY = 10
TREASURE_VALUE = 100

NUM_TRAPS = 3
NUM_KEYS = 2
NUM_CHESTS = 2
NUM_SHOVELS = 1

FRUIT_NAMES = [
    "carrot", "apple", "strawberry", "cherry",
    "watermelon", "radish", "cucumber", "meatball",
]


class Item:


    def __init__(self, name, value=0, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def on_pickup(self, state):

        state.player.add_points(self.value)
        if self.value:
            sign = "+" if self.value >= 0 else ""
            print(f"You found a {self.name}, {sign}{self.value} points.")
        state.player.add_to_inventory(self.name)
        state.g.clear(state.player.pos_x, state.player.pos_y)
        state.register_collected()


class Fruit(Item):


    def __init__(self, name):
        super().__init__(name, value=FRUIT_VALUE, symbol="?")


class Trap(Item):


    def __init__(self):
        super().__init__("trap", value=-TRAP_PENALTY, symbol="^")

    def on_pickup(self, state):
        state.player.add_points(self.value)
        print(f"You stepped on a trap! {self.value} points.")


class Key(Item):


    def __init__(self):
        super().__init__("key", value=0, symbol="K")

    def on_pickup(self, state):
        super().on_pickup(state)
        print("You picked up a key.")


class Chest(Item):

    def __init__(self):
        super().__init__("chest", value=0, symbol="C")

    def on_pickup(self, state):
        if state.player.has_item("key"):
            state.player.remove_from_inventory("key")
            state.player.add_points(TREASURE_VALUE)
            state.player.add_to_inventory("treasure")
            state.g.clear(state.player.pos_x, state.player.pos_y)
            print(
                f"You unlocked the chest with a key and found a treasure! "
                f"+{TREASURE_VALUE} points."
            )
            state.register_collected()
        else:
            print("The chest is locked. You need a key to open it.")


class Shovel(Item):

    def __init__(self):
        super().__init__("shovel", value=0, symbol="S")

    def on_pickup(self, state):
        super().on_pickup(state)
        print("You picked up a shovel. Walk into a wall to dig through it!")


class Exit(Item):

    def __init__(self):
        super().__init__("exit", value=0, symbol="E")

    def on_pickup(self, state):
        if state.items_left <= 0:
            state.win()
        else:
            print("The exit seems to be locked. Collect everything on the map first.")


def make_starting_items():
    items = [Fruit(name) for name in FRUIT_NAMES]
    items += [Trap() for _ in range(NUM_TRAPS)]
    items += [Key() for _ in range(NUM_KEYS)]
    items += [Chest() for _ in range(NUM_CHESTS)]
    items += [Shovel() for _ in range(NUM_SHOVELS)]
    return items


def place_randomly(grid, item):
    x, y = grid.get_random_empty_position()
    grid.set(x, y, item)
    return item


def randomize(grid, items):
    for item in items:
        place_randomly(grid, item)


def place_exit(grid):
    return place_randomly(grid, Exit())


def spawn_random_fruit(grid):
    return place_randomly(grid, Fruit(random.choice(FRUIT_NAMES)))
