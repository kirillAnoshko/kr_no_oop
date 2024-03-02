import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы для окна и клеток
WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Класс клетки
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = self.col * CELL_SIZE
        self.y = self.row * CELL_SIZE
        self.value = None

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect, 2)
        if self.value == 'X':
            pygame.draw.line(screen, WHITE, (self.x + 10, self.y + 10), (self.x + CELL_SIZE - 10, self.y + CELL_SIZE - 10), 2)
            pygame.draw.line(screen, WHITE, (self.x + CELL_SIZE - 10, self.y + 10), (self.x + 10, self.y + CELL_SIZE - 10), 2)
        elif self.value == 'O':
            pygame.draw.circle(screen, WHITE, (self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2), CELL_SIZE // 2 - 10, 2)


# Класс игры
class Game:
    def __init__(self, mode):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
        self.turn = 'X'
        self.mode = mode

    def check_winner(self):
        for row in range(ROWS):
            if all(self.board[row][col].value == 'X' for col in range(COLS)):
                return 'X'
            if all(self.board[row][col].value == 'O' for col in range(COLS)):
                return 'O'

        for col in range(COLS):
            if all(self.board[row][col].value == 'X' for row in range(ROWS)):
                return 'X'
            if all(self.board[row][col].value == 'O' for row in range(ROWS)):
                return 'O'

        if all(self.board[i][i].value == 'X' for i in range(ROWS)):
            return 'X'
        if all(self.board[i][i].value == 'O' for i in range(ROWS)):
            return 'O'

        if all(self.board[i][ROWS - i - 1].value == 'X' for i in range(ROWS)):
            return 'X'
        if all(self.board[i][ROWS - i - 1].value == 'O' for i in range(ROWS)):
            return 'O'

        return None

    def bot_move(self):
        empty_cells = [(row, col) for row in range(ROWS) for col in range(COLS) if self.board[row][col].value is None]
        row, col = random.choice(empty_cells)
        self.board[row][col].value = 'O'

    def draw(self):
        for row in self.board:
            for cell in row:
                cell.draw(self.screen)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.mode == 'player':
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                cell = self.board[row][col]
                if not cell.value:
                    cell.value = self.turn
                    self.turn = 'O' if self.turn == 'X' else 'X'
            if self.mode == 'bot' and self.turn == 'O':
                self.bot_move()
                self.turn = 'X'

    def run(self):
        while True:
            self.screen.fill(BLACK)
            self.draw()
            pygame.display.flip()
            self.handle_event()
            winner = self.check_winner()
            if winner:
                print(f'Winner is {winner}')
                pygame.time.wait(3000)  # Пауза после объявления победителя
                pygame.quit()
                sys.exit()


# Инициализация игры и запуск игрового цикла
if __name__ == '__main__':
    mode = input("Выберите режим игры ('player' - против другого игрока, 'bot' - против бота): ")
    game = Game(mode)
    game.run()
