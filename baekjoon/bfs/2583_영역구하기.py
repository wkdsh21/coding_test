import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
m, n, k = map(int, input().split())
num_list = [[0] * n for _ in range(m)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            num_list[y][x] = 1

deq = deque()
answer = []
for i in range(m):
    for j in range(n):
        if num_list[i][j] == 0:
            deq.append((i, j))
            num_list[i][j] = 1
            count = 1
            while deq:
                y, x = deq.popleft()
                for dy, dx in dxdy:
                    if (
                        0 <= dy + y < m
                        and 0 <= dx + x < n
                        and num_list[dy + y][dx + x] == 0
                    ):
                        deq.append((dy + y, dx + x))
                        num_list[y + dy][x + dx] = 1
                        count += 1
            answer.append(count)
answer.sort()
print(len(answer))
print(" ".join(map(str, answer)))
