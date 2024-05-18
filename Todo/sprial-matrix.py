import math


def gen_matrix(n):
    matrix = [[0 for a in range(n)] for i in range(n)]
    s_num = 1
    for round in range(math.ceil(n/2)):
        lenth = n - 1 - round * 2
        if lenth == 0:
            matrix[round][round] = s_num
            break
        for i in range(lenth):
            matrix[round][round + i] = s_num + i
            matrix[round + i][-(round + 1)] = s_num + lenth + i
            matrix[-(round+1)][-(round+i+1)] = s_num + lenth * 2 + i
            matrix[-(round + i + 1)][round] = s_num + lenth * 3 + i
        s_num += 4 * lenth

    for col in matrix:
        print(col)


if __name__ == '__main__':
    gen_matrix(5)
