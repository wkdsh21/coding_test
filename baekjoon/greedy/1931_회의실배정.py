import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: (x[0], x[1]))
dp = [0] * n
dp[0] = 1
heap = [(li[0][1], 0)]
# 우선순위큐 쓰면됨

for i in range(1, n):
    temp = []
    while heap and heap[0][0] <= li[i][0]:
        temp.append(heappop(heap))
    if temp:
        # pop된 튜플들의 dp값이랑 기존의 dp최댓값 비교
        dp[i] += max(max([dp[i[1]] for i in temp]) + 1, dp[i - 1])
    else:
        dp[i] += dp[i - 1]
    heappush(heap, (li[i][1], i))

print(max(dp))
