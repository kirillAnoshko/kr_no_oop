from os import system
from random import choice


class Player:
    def __init__(self, is_automatic=True, image=None) -> None:
        self.image = image
        self.is_automatic = is_automatic

    def make_move(self, field):        
        if not self.is_automatic:
            while True:
                try:
                    cell_number = int(input(f'Введите номер клетки для хода {self.image}: '))
                except ValueError:
                    print('Ошибка! Номер клетки должен быть целым числом')
                    continue
                if cell_number < 1 or cell_number > 9:
                    print('Ошибка! Номер клетки должен быть от 0 до 9 вкл.')
                    continue
                index = cell_number - 1
                if isinstance(field.cells[index]):
                    print('Ошибка! Эта клетка занята!')
                break
        field.cells[index] = self.image

        if self.is_automatic:
            free_cells_indexes = []
            for i in range(9):
                if isinstance(field.cells[i], int):
                    free_cells_indexes.append(i)
            random_index = choice(free_cells_indexes)
            field.cells[index] = self.image


class Field:
    def __init__(self) -> None:
        self.cells = [i for i in range(1, 10)]

    def draw(self):
        system('cls')
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])


class Game:
    def __init__(self) -> None:
        self.player_1 = Player(image='X', is_automatic=False)
        self.player_2 = Player(image='0', is_automatic=False)
        self.field = Field()

    def get_winner(self) -> str:
        for i in range(0, 7, 3):
            if self.field.cells[i] == self.field.cells[i + 1] == self.field.cells[i + 2]:
                return self.field.cells[i]

        for i in range(3):
            if self.field.cells[i] == self.field.cells[i + 3] == self.field.cells[i + 2]:
                return self.field.cells[i]

        return ''

    def run(self):
        turn = 1
        while True:
            if turn > 9:
                print('Ничья!')
                break
            self.field.draw()
            if turn % 2: # Нечетный ход
                self.player_1.make_move(self.field)
            else: # Четный ход
                self.player_2.make_move(self.field)
            turn += 1
            winner = self.get_winner()
            if winner:
                print(f'Победил {winner}')


class App:
    def __init__(self) -> None:
        self.game = Game()
        self.game.run()


App()
