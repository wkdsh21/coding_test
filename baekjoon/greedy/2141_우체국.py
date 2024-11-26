import sys
from heapq import heappush, heappop

input = sys.stdin.readline
# 위치 정렬후 맨왼쪽부터해서 양쪽의 사람수를 비교함 사람수가 많은쪽으로 이동하면 무조건 최소값에 가까워지기때문
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: x[0])
right = sum(i[1] for i in li) - li[0][1]
left = li[0][1]

for i in range(n):
    if left >= right:
        print(li[i][0])
        break
    if i != n - 1:
        left += li[i + 1][1]
        right -= li[i + 1][1]
