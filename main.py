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


class Automata:

    def __init__(self, width, height, N, D, R, X, P_high, P_low, T):

        self.width = width
        self.height = height
        self.grid = [[Cell() for j in range(width)] for i in range(height)]

        self.sick = int(D * N)
        self.infectionTime = X
        self.high_prob = P_high
        self.low_prob = P_low
        self.threshold = int(T * N)

        positions = []
        n_creatures = N
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
            self.grid[i][j].put(c)
            creatures.append(c)

        chosen = random.choices(creatures, k=self.sick)
        for c in chosen:
            c.infection = X

        chosen = random.choices(creatures, k=int(R * N))
        for c in chosen:
            c.steps = 10

    def advance(self):
        for i in range(self.height):
            for j in range(self.width):
                c = self.grid[i][j].creature
                if c is not None:
                    if self.sick < self.threshold:
                        p = self.high_prob
                    else:
                        p = self.low_prob
                    c.update(self.grid, i, j, p, self.infectionTime)
                    dj, di = actions[random.randint(1, 9)]
                    new_i = (i + di * c.steps) % self.height
                    new_j = (j + dj * c.steps) % self.width
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
        self.infection = 0
        self.steps = 1

    def update(self, grid, i, j, probability, infectionTime):
        if self.infection > 0:
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


if __name__ == '__main__':
    automata = Automata(width=200, height=200, N=5000, P_high=0.3, P_low=0.1, D=0.1, T=10)
