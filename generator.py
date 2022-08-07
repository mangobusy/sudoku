from stat import filemode
import numpy as np
import os
import math
import random


def check(x, y, siz, ans, target):
    for i in range(1, siz * siz + 1):
        ans[target[x][i]] = ans[target[i][y]] = 0
    for i in range(((x - 1) // siz) * siz + 1, ((x - 1) // siz) * siz + siz + 1):
        for j in range(((y - 1) // siz) * siz + 1, ((y - 1) // siz) * siz + siz + 1):
            ans[target[i][j]] = 0


def generator(n, p):
    # generate a n^2*n^2 square sudoku(maybe unsolvable)
    # important!
    x = np.zeros(shape=[n * n + 1, n * n + 1], dtype=int)  # numpy.zeros(shape,dtype=float)
    # the ultimate return value                  # shape: 创建新数组的形状（维度）
    ck = np.zeros(n * n + 1, dtype=bool)  # dtype: 创建新数组的数据类型
    # used to check whether i is available
    for i in range(1, n * n + 1):
        for j in range(1, n * n + 1):
            if random.random() < p:
                for k in range(1, n * n + 1):
                    ck[k] = 1
                check(i, j, n, ck, x)
                if np.amax(ck) == 0:
                    continue
                while (1):
                    t = random.randint(1, n * n)
                    if ck[t]:
                        x[i][j] = t
                        break
    return x


def prt(x, filename=''):
    # print a pretty 2-D numpy 1-based
    if filename == '':
        print(x.shape[0] - 1)
        for i in range(1, x.shape[0]):
            for j in range(1, x.shape[1]):
                print(x[i][j], end=" ")
            print("")
        return
    with open(filename + ".txt", "w+") as f:
        f.write(str(x.shape[0] - 1) + '\n')
        for i in range(1, x.shape[0]):
            for j in range(1, x.shape[1]):
                f.write(str(x[i][j]) + " ")
            f.write('\n')


def main():
    prt(generator(5, 0.2))


if __name__ == "__main__":
    main()

print(main)