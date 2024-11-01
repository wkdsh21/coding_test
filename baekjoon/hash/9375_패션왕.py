import sys
from collections import defaultdict

input = sys.stdin.readline

test_num = int(input())

for _ in range(test_num):
    n = int(input())
    answer = 1
    clothes = defaultdict(int)
    for _ in range(n):
        name, category = input().split()
        clothes[category] += 1

    for value in clothes.values():
        answer *= value + 1

    print(answer - 1)
