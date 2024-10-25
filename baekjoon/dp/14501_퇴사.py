import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
t, p = [-1], [-1]
for i in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)
deq = deque()
answer = 0
for i in range(1, n + 1):
    deq.append((i, 0))
    while deq:
        day, sum_result = deq.popleft()
        if day + t[day] - 1 <= n:
            sum_result += p[day]

        if day + t[day] - 1 < n:
            for i in range(day + t[day], n + 1):
                deq.append((i, sum_result))
        else:
            answer = max(answer, sum_result)
            continue
print(answer)
