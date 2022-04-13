import random


actions = {
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (-1, 0),
    5: (0, 0),
    6: (1, 0),
    7: (-1, 1),
    8: (0, 1),
    9: (1, 1)
}

# NORTH_WEST = 1
# NORTH = 2
# NORTH_EAST = 3
# EAST = 4
# CURRENT = 5
# WEST = 6
# SOUTH_WEST = 7
# SOUTH = 8
# SOUTH_EAST = 9


class Position:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class Automata:

    def __init__(self, width, height, N, D, R, P_high, P_low, T):

        self.width = width
        self.height = height
        self.grid = [[Cell() for j in range(width)] for i in range(height)]
        positions = []
        creatures = []
        n_creatures = N

        while n_creatures > 0:
            i = random.randint(0, self.width)
            j = random.randint(0, self.height)
            pos = (i, j)
            if pos not in positions:
                positions.append(pos)
                n_creatures -= 1

        for (i, j) in positions:
            c = Creature()
            self.grid[i][j].put(c)
            creatures.append(c)

        chosen = random.choices(creatures, k=int(D * N))
        for c in chosen:
            c.isInfected = True

        chosen = random.choices(creatures, k=int(R * N))
        for c in chosen:
            c.steps = 10

    def infection(self, i, j):
        for x in range(-1, 2):
            for y in range(-1, 2):
                cell = self.grid[i][j]
                if not cell.isEmpty():
                    if cell.creature.isInfected: # KAN ANI!



    def advance(self):
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[i][j].creature
                if c is not None:
                    if not c.isInfected:
                        c.isInfected = self.infection(i, j)
                    x, y = actions[random.randint(1, 9)]
                    new_i = (i + x * c.steps) % self.height
                    new_j = (j + y * c.steps) % self.width
                    if self.grid[new_i][new_j].isEmpty():
                        self.grid[new_i][new_j].put(c)
                        self.grid[i][j].clear()
                    else:
                        raise 'implement what to do when destination cell is not empty.'


class Cell:

    def __init__(self):
        self.creature = None

    def put(self, creature):
        self.creature = creature

    def clear(self):
        self.creature = None

    def isEmpty(self):
        return True if self.creature is None else False


class Creature:

    def __init__(self):
        self.isInfected = False
        self.steps = 1


# class Creature:
#
#     def __init__(self, pos):
#         self.isInfected = False
#         self.speed = 0
#         self.position = pos
#
#     def move(self, direction, grid):
#         new_i = self.position.i
#         new_j = self.position.j
#         if direction == NORTH:
#             new_j = self.position.j - self.speed
#         if direction == NORTH_EAST:
#             new_i = self.position.i + self.speed
#             new_j = self.position.j - self.speed
#         if direction == NORTH_WEST:
#             new_i = self.position.i - self.speed
#             new_j = self.position.j - self.speed
#         if direction == SOUTH:
#             new_j = self.position.j + self.speed
#         if direction == SOUTH_EAST:
#             new_i = self.position.i + self.speed
#             new_j = self.position.j + self.speed
#         if direction == SOUTH_WEST:
#             new_i = self.position.i - self.speed
#             new_j = self.position.j + self.speed
#         if direction == EAST:
#             new_i = self.position.i - self.speed
#         if direction == WEST:
#             new_i = self.position.i + self.speed
#         new_i = new_i % len(grid[0])
#         new_j = new_j % len(grid)
#         if grid[new_i][new_j] is not None:
#             grid[self.position.i][self.position.j] = None
#             self.position.i = new_i
#             self.position.j = new_j
#             grid[new_i][new_j] = self
#         else:
#             raise 'implement what to do when destination cell is not empty.'

if __name__ == '__main__':
    automata = Automata(width=200, height=200, N=5000, P_high=0.3, P_low=0.1, D=0.1, T=10)
