import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
game_sequence = [int(input()) for _ in range(n)]
visit = [0] * n

deq = deque([game_sequence[0]])
visit[0] = 1
count = 0
while True:
    temp = deq.popleft()
    next = game_sequence[temp]
    count += 1
    if temp == k:
        print(count)
        break

    if visit[next] == 0:
        deq.append(next)
        visit[next] = 1
    else:
        print(-1)
        break
