import sys
import bisect

# 해쉬 이용하면 훨씬 간단하고 빠름
input = sys.stdin.readline
answer = []
n = int(input())
n_list = [int(i) for i in input().split()]
m = int(input())
m_list = [int(i) for i in input().split()]

n_list.sort()
for i in m_list:
    temp = bisect.bisect_left(n_list, i)
    if temp != len(n_list) and i == n_list[bisect.bisect_left(n_list, i)]:
        answer.append(1)
    else:
        answer.append(0)

for i in answer:
    print(i, end=" ")
