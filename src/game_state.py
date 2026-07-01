
from src.grid import Grid
from src.player import Player
from src import pickups

class GameState:

    def __init__(self):
        self.g = Grid()
        self.player = Player(self.g.width // 2, self.g.height // 2)
        self.g.set_player(self.player)
        self.g.make_walls()

        starting_items = pickups.make_starting_items()
        pickups.randomize(self.g, starting_items)
        pickups.place_exit(self.g)


        self.items_left = sum(
            1 for item in starting_items if not isinstance(item, pickups.Trap)
        )

        self.moves_taken = 0
        self.is_running = True
        self.has_won = False

    def register_collected(self):

        self.items_left -= 1

    def win(self):
        self.has_won = True
        self.is_running = False