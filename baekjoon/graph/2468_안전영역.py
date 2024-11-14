import sys
from collections import deque

input = sys.stdin.readline
dxy = ((1, 0), (-1, 0), (0, -1), (0, 1))
n = int(input())
area = [[int(i) for i in input().rstrip().split()] for i in range(n)]
max_height = max([max(i) for i in area])
deq = deque()
answer = 1
for height in range(1, max_height):
    visit = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and area[i][j] > height:
                count += 1
                deq.append((i, j))
                visit[i][j] = 1
                while deq:
                    y, x = deq.popleft()
                    for dx, dy in dxy:
                        if (
                            0 <= dx + x < n
                            and 0 <= dy + y < n
                            and visit[dy + y][dx + x] == 0
                            and area[dy + y][dx + x] > height
                        ):
                            deq.append((dy + y, dx + x))
                            visit[dy + y][dx + x] = 1
    answer = max(answer, count)
print(answer)
