import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())

    yx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    field = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    target = [list(map(int, input().split())) for _ in range(k)]
    for x, y in target:
        field[y][x] = 1

    queue = deque()
    count = 0
    while True:
        check = 0
        for x, y in target:
            if field[y][x] == 1 and visit[y][x] == 0:
                queue.append([x, y])
                visit[y][x] = 1
                check = 1
                break
        if check == 0:
            break
        count += 1
        while queue:
            temp = queue.popleft()
            for y, x in yx:
                if (
                    0 <= y + temp[1] < n
                    and 0 <= x + temp[0] < m
                    and visit[y + temp[1]][x + temp[0]] == 0
                    and field[y + temp[1]][x + temp[0]] == 1
                ):
                    queue.append([x + temp[0], y + temp[1]])
                    visit[y + temp[1]][x + temp[0]] = 1
    print(count)
