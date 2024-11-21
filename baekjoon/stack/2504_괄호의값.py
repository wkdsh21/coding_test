import sys

input = sys.stdin.readline

input_str = list(input().rstrip())
stack = []
answer = 0
times = 1
num = 0
check = 0
for i in input_str:
    if i == "(" or i == "[":
        stack.append(i)
        num = len(stack)
        if i == "(":
            times *= 2
        else:
            times *= 3
    elif i == ")":
        if not stack or stack[-1] != "(":
            check = 1
            break
        times //= 2
        if num == len(stack):
            answer += times * 2
        stack.pop()
    elif i == "]":
        if not stack or stack[-1] != "[":
            check = 1
            break
        times //= 3
        if num == len(stack):
            answer += times * 3
        stack.pop()


if check or stack:
    print(0)
else:
    print(answer)
