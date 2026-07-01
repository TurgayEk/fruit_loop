class Player:

    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

        self.__score = 0

        self.inventory = []

    def move(self, dx, dy):

        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        target_x = self.pos_x + dx
        target_y = self.pos_y + dy
        return not grid.is_wall(target_x, target_y)

    # --- Poäng ------------------------------------------#

    def add_points(self, amount):
       self.__score += amount

    def get_score(self):
        return self.__score

    # --- Inventory -----------------------------------------------------------
    def add_to_inventory(self, name):
        self.inventory.append(name)

    def has_item(self, name):
        return name in self.inventory

    def remove_from_inventory(self, name):
        if name in self.inventory:
            self.inventory.remove(name)

    def use_shovel(self):

        if self.has_item("shovel"):
            self.remove_from_inventory("shovel")
            return True
        return False

    def print_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return

        print("Inventory:")
        for thing in self.inventory:
            print(f" - {thing}")
