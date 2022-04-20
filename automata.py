import random
import matplotlib.pyplot as plt
from state import State


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

    def __init__(self, i, j, healing_time):
        self.steps = 1
        self.infection = 0
        self.pos = (i, j)
        self.healing_time = healing_time

    def is_quick(self):
        return self.steps > 1

    def is_infected(self):
        return self.infection > 0

    def move(self, i, j):
        self.pos = (i, j)

    def update(self, grid, probability):
        if self.infection == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    ni = self.pos[0] + x
                    nj = self.pos[1] + y
                    if ni < 0 or ni > 199 or nj < 0 or nj > 199:
                        continue
                    neighbor = grid[ni][nj].creature
                    if neighbor is not None and neighbor.infection > 0:
                        if random.random() < probability:
                            self.infection = self.healing_time
                            return 1
        else:
            self.infection -= 1


class Automata:

    def __init__(self, app):

        self.state = State()
        self.app = app
        self.width = 200
        self.height = 200

        self.n_creatures = 0
        self.n_sick = 0
        self.healing_time = 0
        self.quick_creatures = 0
        self.high_prob = 0.0
        self.low_prob = 0.0
        self.threshold = 0.0

        self.grid = []
        self.creatures = []
        self.trand = []

    def __create_grid(self):
        grid = [[Cell() for j in range(200)] for i in range(200)]
        positions = [(i, j) for j in range(200) for i in range(200)]
        n_creatures = self.n_creatures
        while n_creatures > 0:
            (i, j) = random.choice(positions)
            c = Creature(i, j, self.healing_time)
            grid[i][j].put(c)
            self.creatures.append(c)
            positions.remove((i, j))
            n_creatures -= 1
        chosen = random.choices(self.creatures, k=self.n_sick)
        for c in chosen:
            c.infection = self.healing_time
        chosen = random.choices(self.creatures, k=self.quick_creatures)
        for c in chosen:
            c.steps = 10
        return grid

    def set(self, N, D, X, R, P_high, P_low, T):
        self.n_creatures = N
        self.n_sick = int(D * N)
        self.healing_time = X
        self.quick_creatures = int(R * N)
        self.high_prob = P_high
        self.low_prob = P_low
        self.threshold = int(T * N)
        self.grid = self.__create_grid()

    def __plot(self):
        plt.figure()
        plt.title('Number of infected creatures per generation')
        plt.xlabel('Generation')
        plt.ylabel('Infected')
        plt.plot(list(range(len(self.trand))), self.trand)
        plt.savefig("InfectedPerGeneration.png")

    def __advance(self):
        self.app.frame.delete('all')
        for c in self.creatures:
            i, j = c.pos
            if c.infection > 0:
                if c.steps == 10:
                    color = '#ff0000'
                else:
                    color = '#ffa500'
            elif c.steps == 10:
                color = '#00ffff'
            else:
                color = '#ffffff'
            x0 = i * 4 - 1
            y0 = j * 4 - 1
            x1 = (i + 1) * 4 + 1
            y1 = (j + 1) * 4 + 1
            self.app.frame.create_rectangle(x0, y0, x1, y1, fill=color)
        p = self.high_prob if self.n_sick < self.threshold else self.low_prob
        for c in self.creatures:
            c.update(self.grid, p)
            i, j = c.pos
            for _ in range(5):
                dj, di = random.randint(-1, 1), random.randint(-1, 1)
                new_i = (i + di * c.steps) % self.height
                new_j = (j + dj * c.steps) % self.width
                if new_i == i and new_j == j:
                    break
                if self.grid[new_i][new_j].isEmpty():
                    c.move(new_i, new_j)
                    self.grid[new_i][new_j].put(c)
                    self.grid[i][j].clear()
                    break
        count_infected = 0
        for c in self.creatures:
            if c.infection > 0:
                count_infected += 1
        self.n_sick = count_infected

    def __loop(self):
        if self.state.is_running:
            self.app.n_sick.delete(0, 'end')
            self.app.n_sick.insert(0, self.n_sick)
            self.app.distribution.delete(0, 'end')
            dist = str(round(self.n_sick / self.n_creatures, 2)) + '%'
            self.app.distribution.insert(0, dist)
            self.app.capacity.delete(0, 'end')
            cap = str(round(self.n_sick / self.threshold, 2)) + '%'
            self.app.capacity.insert(0, cap)
            self.trand.append(self.n_sick)
            self.__advance()
        self.app.window.after(100, self.__loop)

    def run(self):
        self.state.setRunning()
        self.app.window.after(100, self.__loop)

    def pause(self):
        self.state.setPaused()

    def stop(self):
        self.app.frame.delete('all')
        self.state.setStopped()
        self.grid = []
        self.creatures = []
        self.__plot()
        self.trand = []
