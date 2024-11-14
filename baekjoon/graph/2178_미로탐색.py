import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(n)]
yx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
deq = deque([(0, 0, 1)])
# miro list에 직접 거리를 넣어도됨 +1씩해서
while deq:
    temp = deq.popleft()
    for dy, dx in yx:
        y = dy + temp[0]
        x = dx + temp[1]
        if 0 <= y < n and 0 <= x < m and miro[y][x] == 1:
            miro[y][x] = 2
            deq.append((y, x, temp[2] + 1))
            if y == n - 1 and x == m - 1:
                print(temp[2] + 1)
