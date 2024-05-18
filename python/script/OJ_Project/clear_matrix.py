"""
一个向右和向下无限延伸的行和列的表格，以及初始三枚硬币。三枚硬币放在表格的左上角。如下图一所示。
|*|*| |...
|*| | |...
| | | |...
...
游戏操作。我们可以取走一枚硬币，仅当这枚硬币正右方和正下方的格子是空的——因为在取走这枚硬币的同时，还必须在这枚硬币的右边和下边的格子里补上两枚硬币。比如，如果你拿掉了上方第二个硬币，你需要按下图二的方式，马上补上两枚。我们假设可以动用无限多的硬币。
问题，你是否能设计出巧妙地流程，把左上2×2的格子中的硬币全部提走，(经评论提醒有歧义，补充)最终仅留4个空格？
"""
from functools import reduce

import colorama as colorama

colorama.init(autoreset=True)

class Matrix:
    def __init__(self):
        self.order = 2
        self.matrix = list()
        self.gen_matrix()

    def gen_matrix(self):
        self.matrix = [[0 for y in range(self.order + 1)] for x in range(self.order + 1)]
        self.matrix[0][0] = self.matrix[0][1] = self.matrix[1][0] = 1
        # for raw in range(self.order):
        #     self.matrix.append([])
        #     for column in range(self.order):
        #         self.matrix[raw].append(0)

    def print_matrix(self, coordinate=None):
        x, y = coordinate if coordinate else [0, 0]
        print("-" * self.order * 3)
        for raw in range(self.order + 1):
            for column in range(self.order + 1):
                print(self.matrix[raw][column], end=" ")
                if [x, y] == [raw, column]:
                    print("\b\b" + '\033[1;37;46m' + str(self.matrix[x][y]), end=" ")
            print()

    def grow_matrix(self, expand=1):
        for i in range(expand):
            self.matrix.append([0 for x in range(self.order + expand + 1)])
        for i in range(self.order + 1):
            self.matrix[i].extend([0 for x in range(expand)])
        self.order += expand

    def continue_game(self):
        if reduce(lambda x, y: x + y, self.matrix[0][:2] + self.matrix[1][:2]) == 0:
            return False
        return True

    def check_move(self, coordinate):
        x, y = coordinate
        if self.matrix[x+1][y] | self.matrix[x][y+1]:
            raise Exception(f"the [{x}, {y}] can't move")

    def move_coin(self, coordinate):
        x, y = coordinate
        if max(coordinate) > self.order:
            raise Exception("over range")
        if self.matrix[x][y] != 1:
            raise Exception(f"the [{x}, {y}] is null")
        if max(coordinate) == self.order:
            self.grow_matrix()
        self.check_move(coordinate)

        self.matrix[x][y] = 0
        self.matrix[x+1][y] = self.matrix[x][y+1] = 1

        self.print_matrix(coordinate)

    def choice_coin(self):
        pass


if __name__ == '__main__':
    m = Matrix()
    m.print_matrix()
    # m.move_coin([0, 1])
    # m.move_coin([1, 1])
    # m.move_coin([1, 0])
    # m.move_coin([0, 0])
    #
    # m.move_coin([1, 2])
    # m.move_coin([2, 2])
    # m.move_coin([2, 1])
    # m.move_coin([1, 1])
    x, y = 0, 0
    for time in range(2):
        m.move_coin([x, y+1])
        m.move_coin([x+1, y+1])
        m.move_coin([x+1, y])
        m.move_coin([x, y])
        x += 1
        y += 1
        print(f"the {time}th over")
    m.grow_matrix(expand=2)
    m.print_matrix()

