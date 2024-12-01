import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

deq = deque()
deq.append((1, 0))
visit[1] = -1

while deq:
    num, length = deq.popleft()
    for i in graph[num]:
        if not visit[i]:
            visit[i] = length + 1
            deq.append((i, length + 1))

visit_max = max(visit)
print(visit.index(visit_max), visit_max, visit.count(visit_max))
