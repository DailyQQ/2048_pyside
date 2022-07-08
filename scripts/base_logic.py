import random
import numpy


# Константа поля, 4х4
N = 4


class GameLogic:
    """Создание игровой логики"""

    def __init__(self):
        """ Создание сетки"""
        self.grid = numpy.zeros((N, N), dtype=int)

    # def __str__(self):
    #     return str(self.grid)

    def new_number(self, k=1):
        """генерация числа"""
        position_ = list(zip(*numpy.where(self.grid == 0)))

        for position_ in random.sample(position_, k=k):
            if random.random() <= 0.1:
                self.grid[position_] = 4
            else:
                self.grid[position_] = 2

    @staticmethod
    def get_number(initial_pos):
        """"""
        initial_pos_n = initial_pos[initial_pos != 0]
        initial_pos_n_sum = []
        skip = False

        for i in range(len(initial_pos_n)):
            if skip:
                skip = False
                continue
            if i != len(initial_pos_n) - 1 and initial_pos_n[i] == initial_pos_n[i + 1]:
                new_position = initial_pos_n[i] * 2
                skip = True
            else:
                new_position = initial_pos_n[i]

            initial_pos_n_sum.append(new_position)

        return numpy.array(initial_pos_n_sum)

    def move_mechanics(self, move):
        for i in range(N):
            if move in 'lr':
                initial_pos = self.grid[i, :]
            else:
                initial_pos = self.grid[:, i]

            flipped = False
            if move in 'rd':
                flipped = True
                initial_pos = initial_pos[::-1]

            initial_pos_n = self.get_number(initial_pos)

            new_position = numpy.zeros_like(initial_pos)
            new_position[:len(initial_pos_n)] = initial_pos_n

            if flipped:
                new_position = new_position[::-1]

            if move in 'lr':
                self.grid[i, :] = new_position
            else:
                self.grid[:, i] = new_position

    def play_(self):
        self.new_number(k=2)
        while True:
            print(self.grid)
            cmd = input()
            if cmd == 'q':
                break
            old_grid = self.grid.copy()
            self.move_mechanics(cmd)
            if all((self.grid ==old_grid).flatten()):
                continue
            self.new_number()

    def game_over(self, old_grid):

        for move in 'lrud':
            self.make_move(move)
            if not all((self.grid == old_grid).flatten()):
                self.grid = old_grid
                return False
        return True



if __name__ == '__main__':
    game = GameLogic()
    game.play_()