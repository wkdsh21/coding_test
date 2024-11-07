import sys
from collections import deque
import re

input = sys.stdin.readline
t = int(input())


# 스택과 큐의 차이점
# deque는 둘다
# 그래서 시간복잡도가 양쪽다 1
# RR 을 지우면 더빨라질수있음
def ac_func():
    ac = input().rstrip()
    n = int(input())
    num_deq = deque(re.findall(r"\d+", input().rstrip()))
    reversed = False
    for j in ac:
        if j == "R":
            reversed = not reversed
        else:
            if num_deq:
                if reversed:
                    num_deq.pop()
                else:
                    num_deq.popleft()
            else:
                print("error")
                return
    if reversed:
        num_deq = list(num_deq)[::-1]
    print(f'[{",".join(num_deq)}]')


for i in range(t):
    ac_func()
