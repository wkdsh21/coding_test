import sys

input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
for i in sorted(num_list, reverse=True):
    print(i)
