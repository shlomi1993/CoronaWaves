import tkinter as tk
import time
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


class Cell:
    def __init__(self):
        self.creature = None

    def put(self, creature):
        self.creature = creature

    def get(self):
        return self.creature

    def clear(self):
        self.creature = None

    def isEmpty(self):
        return True if self.creature is None else False


class Creature:
    def __init__(self):
        self.infection = 0
        self.steps = 1

    def update(self, grid, i, j, probability, infectionTime):
        if self.infection == 1:
            self.infection -= 1
            return -1
        if self.infection > 1:
            self.infection -= 1
        else:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    neighbor = grid[i + x][j + y].creature
                    if neighbor is not None and neighbor.infection > 0:
                        if random.random() < probability:
                            self.infection = infectionTime
                            return 1
        return 0


class Grid:
    def __init__(self, bg, fg, N, D, R, X, P_high, P_low, T):

        self.width = 200
        self.height = 200
        self.amountOfCreature = N
        self.quickerCreatures = R
        self.infectionTime = X
        self.high_prob = P_high
        self.low_prob = P_low
        self.threshold = int(T * N)
        self.sick = int(D * N)

        self.grid = [[Cell() for j in range(200)] for i in range(200)]

        self.bg = bg
        self.fg = fg
        self.activeAreaColor = '#404040'
        self.cellSide = 5
        self.grid_space: tk.Canvas = None

        self.init_grid()
        self.state = 'p'  # 'p': paused, 'r': running

    def getGrid(self):
        self.grid_space = tk.Canvas(
            bg=self.bg,
            bd=0,
            highlightthickness=0,
            width=500
        )

        self.grid_space.create_rectangle(0, 0, self.cellSide * 200, self.cellSide * 200,
                                         tags='activeArea', fill=self.activeAreaColor,
                                         outline=self.activeAreaColor)
        return self.grid_space

    def init_grid(self):
        positions = []
        n_creatures = self.amountOfCreature
        while n_creatures > 0:
            i = random.randint(0, self.width)
            j = random.randint(0, self.height)
            pos = (i, j)
            if pos not in positions:
                positions.append(pos)
                n_creatures -= 1

        creatures = []
        for (i, j) in positions:
            c = Creature()
            self.grid[i - 1][j - 1].put(c)
            creatures.append(c)

        chosen = random.choices(creatures, k=self.sick)
        for c in chosen:
            c.infection = self.infectionTime

        chosen = random.choices(creatures, k=int(self.quickerCreatures * self.amountOfCreature))
        for c in chosen:
            c.steps = 10

    def CoronaWaves(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].creature:
                    self.grid_space.create_rectangle(i * 5, j * 5, (i + 1) * 5, (j + 1) * 5,
                                                     fill=self.fg, tags='Cell({}{})'.format(i + 1, j + 1))
                else:
                    self.grid_space.delete('Cell({}{})'.format(i + 1, j + 1))
        if self.state == 'r':
            for i in range(self.width):
                for j in range(self.height):
                    c = self.grid[i][j].get()
                    if c is not None:
                        if self.sick < self.threshold:
                            p = self.high_prob
                        else:
                            p = self.low_prob
                        self.sick += c.update(self.grid, i - 1, j - 1, p, self.infectionTime)
                        dj, di = actions[random.randint(1, 9)]
                        new_i = (i + di * c.steps) % self.height
                        new_j = (j + dj * c.steps) % self.width
                        if self.grid[new_i][new_j].isEmpty():
                            self.grid[new_i][new_j].put(c)
                            self.grid[i][j].clear()
        print("finish round")

    #             # else:
    #             #     raise 'implement what to do when destination cell is not empty.'
    def pause(self):
        if self.state == 'r':
            self.state = 'p'

    def resume(self):
        if self.state == 'p':
            self.state = 'r'
            self.gridLoop()

    def gridLoop(self):
        #while self.state == 'r':
            self.grid_space.after_idle(func=self.CoronaWaves)
            time.sleep(0.5)

