from os import system


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

    def run(self):
        while True:
            self.field.draw()
            if: # Нечетный ход
                self.player_1.make_move(self.field)
            else: # Четный ход
                self.player_2.make_move(self.field)


class App:
    def __init__(self) -> None:
        self.game = Game()
        self.game.run()


App()
