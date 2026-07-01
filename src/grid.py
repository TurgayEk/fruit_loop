import random


class Grid:

    width = 36
    height = 12
    empty = "."
    wall = "#"


    def __init__(self):
            self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def get(self, x, y):

        return self.data[y][x]

    def set(self, x, y, value):

        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        self.set(x, y, self.empty)

    def __str__(self):
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs

    def make_walls(self):

        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        wall_row = self.height // 3
        gap_column = self.width // 2
        for x in range(4, self.width - 4):
            if x == gap_column:
                continue
            self.set(x, wall_row, self.wall)

        wall_column = (self.width * 2) // 3
        gap_row = self.height // 2
        for y in range(2, self.height - 2):
            if y == gap_row:
                continue
            self.set(wall_column, y, self.wall)

    def is_wall(self, x, y):

        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        return self.get(x, y) == self.wall

    def get_random_x(self):

        return random.randint(0, self.width - 1)

    def get_random_y(self):

        return random.randint(0, self.height - 1)

    def is_empty(self, x, y):

        return self.get(x, y) == self.empty

    def get_random_empty_position(self):

        while True:
            x = self.get_random_x()
            y = self.get_random_y()
            if self.is_empty(x, y):
                return x, y
