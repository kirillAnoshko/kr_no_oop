import os

EMPTY = '█'


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = EMPTY

    def __str__(self):
        return f'{self.image}'


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = dict()
        self.make_cells()

    def make_cells(self):
        for x in range(1, self.height + 1):
            for y in range(1, self.height + 1):
                self.cells[(x, y)] = Cell(x, y)

    def get_cell(self, x, y) -> Cell:
        return self.cells[(x, y)]

    def draw(self):
        os.system('cls')
        for y in range(1, self.height + 1):
            for x in range(1, self.height + 1):
                print(self.get_cell(x, y), end='')
            print()

screen = Screen(20, 10)
while True:
    #os.system('cls')
    screen.draw()
