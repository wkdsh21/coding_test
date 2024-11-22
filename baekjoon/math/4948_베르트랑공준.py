import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    number = [[True] for _ in range(2 * n + 1)]
    number[0] = False
    number[1] = False
    for i in range(2, 2 * n + 1):
        if number[i]:
            for j in range(2 * i, 2 * n + 1, i):
                number[j] = False
    answer = []
    number[n] = False
    for i in range(n, 2 * n + 1):
        if number[i]:
            answer.append(i)
    print(len(answer))
