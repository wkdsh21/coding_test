import sys
from collections import deque

# 148ms vs 50ms(dfs)
# dfs로 주어진 그래프말고 그래프에서 1인 위치만 뽑아서 새로 리스트만드는게 더빠름
# ex) [2,3] 이어져있는 인덱스만 리스트에 넣기 [0,0,1,1,0,0,0] 이렇게 말고
input = sys.stdin.readline
n = int(input())
route = [list(map(int, input().split())) for _ in range(n)]
answer_route = [[0] * n for _ in range(n)]

deq = deque()

for i in range(n):
    visit = [0] * n
    visit[i] = 1
    for j in range(n):
        if route[i][j] == 1:
            deq.append(j)
            answer_route[i][j] = 1
    while deq:
        temp = deq.popleft()
        if not visit[temp]:
            visit[temp] = 1
        else:
            continue

        for j in range(n):
            if route[temp][j] == 1:
                deq.append(j)
                answer_route[i][j] = 1


print("\n".join([" ".join(map(str, answer_route[i])) for i in range(n)]))
