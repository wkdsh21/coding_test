import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    temp = list(input().rstrip())
    stack = 0
    for j in temp:
        if j == "(":
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            break
    if stack == 0:
        print("YES")
    else:
        print("NO")
