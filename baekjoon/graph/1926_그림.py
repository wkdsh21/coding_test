import sys
from collections import deque

input = sys.stdin.readline

yx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
pictures = [list(map(int, input().split())) for _ in range(n)]
deq = deque()
answer_count = 0
answer_maxpic = 0
# 이중포문으로 돌면서 deq에 넣기
for i in range(n):
    for j in range(m):
        if pictures[i][j] == 1:
            deq.append((i, j))
            pictures[i][j] = 2
            count = 1
            while deq:
                temp = deq.popleft()
                for dy, dx in yx:
                    y = dy + temp[0]
                    x = dx + temp[1]
                    if 0 <= y < n and 0 <= x < m and pictures[y][x] == 1:
                        count += 1
                        deq.append((y, x))
                        pictures[y][x] = 2
            answer_count += 1
            answer_maxpic = max(answer_maxpic, count)
print(answer_count)
print(answer_maxpic)
