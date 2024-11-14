import sys
from math import *

# 986ms
# 출력 형식을 잘봐라 띄어쓰기인지 붙여서 출력인지

input = sys.stdin.readline

n = int(input())

star = [[" "] * n for i in range(n)]


def a(xy, m):
    if m == 3:
        for i in range(xy[0], m + xy[0]):
            star[xy[1]][i] = "*"
            star[m + xy[1] - m // 3][i] = "*"
        for i in range(xy[1], m + xy[1]):
            star[i][m + xy[0] - m // 3] = "*"
            star[i][xy[0]] = "*"
    else:
        for i in range(xy[0], m + xy[0], m // 3):
            a((i, xy[1]), m // 3)
            a((i, m + xy[1] - m // 3), m // 3)
        for i in range(xy[1], m + xy[1], m // 3):
            a((xy[0], i), m // 3)
            a((m + xy[0] - m // 3, i), m // 3)


a((0, 0), n)

for i in range(n):
    print("".join(star[i]))
