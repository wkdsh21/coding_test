import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    num_list = list(map(int, input().split()))
    if num_list[0] == 0:
        break
    else:
        del num_list[0]

    for i in combinations(num_list, 6):
        print(*i)
    print()
