from src.game_state import GameState
from src import pickups

STEP_PENALTY = 1
FERTILE_GROUND_INTERVAL = 25

DIRECTIONS = {
    "w": (0, -1),
    "s": (0, 1),
    "a": (-1, 0),
    "d": (1, 0),
}

def print_status(game_grid, state):
    print("--------------------------------------")
    print(f"You HAVE {state.player.get_score()} points.")
    print(game_grid)

def move_player(state, dx, dy, steps):

    if not state.player.can_move(dx, dy, state.g):
        handle_wall_collision(state, dx, dy)
        return

    state.player.move(dx, dy)
    state.player.add_points(-STEP_PENALTY * steps)  # Krav G
    state.moves_taken += 1

    collect_item_at_player(state)
    maybe_grow_fruit(state)


def collect_item_at_player(state):

    maybe_item = state.g.get(state.player.pos_x, state.player.pos_y)
    if isinstance(maybe_item, pickups.Item):
        maybe_item.on_pickup(state)


def handle_wall_collision(state, dx, dy):

    if state.player.use_shovel():
        target_x = state.player.pos_x + dx
        target_y = state.player.pos_y + dy
        state.g.clear(target_x, target_y)
        print("You dug through the wall with your shovel!")
    else:
        print("There's a wall in the way.")


def maybe_grow_fruit(state):

    if state.moves_taken % FERTILE_GROUND_INTERVAL == 0:
        pickups.spawn_random_fruit(state.g)
        print("The ground feels fertile... a new fruit has appeared!")


def parse_command(raw_command):

    command = raw_command.strip().casefold()

    if command in ("q", "x"):
        kind, direction = "quit", None
    elif command == "i":
        kind, direction = "inventory", None
    elif len(command) == 2 and command[0] == "j" and command[1] in DIRECTIONS:
      kind, direction = "jump", command[1]
    elif command in DIRECTIONS:
        kind, direction = "move", command
    else:
        kind, direction = "unknown", None

    return kind, direction

def handle_command(state, raw_command):
    kind, direction = parse_command(raw_command)

    if kind == "quit":
        state.is_running = False
    elif kind == "inventory":
        state.player.print_inventory()
    elif kind == "move":
        dx, dy = DIRECTIONS[direction]
        move_player(state, dx, dy, steps=1)
    elif kind == "jump":
        dx, dy = DIRECTIONS[direction]
        move_player(state, dx * 2, dy * 2, steps=2)
    else:
        print("Unknown command. Use W/A/S/D to move, 'i' for inventory, "
              "J + direction to jump (e.g. 'jw'), or Q/X to quit.")


def start(state):
    while state.is_running:
        print_status(state.g, state)

        raw_command = input(
            "Use WASD to move, 'i' for inventory, J+direction to jump, Q/X to quit. "
        )
        handle_command(state, raw_command)


    print_status(state.g, state)
    if state.has_won:
        print("Congratulations, you collected everything and escaped!")
    print(f"Final score: {state.player.get_score()}")
    print("Thank you for playing!")


if __name__ == "__main__":
    game_state = GameState()
    start(game_state)
