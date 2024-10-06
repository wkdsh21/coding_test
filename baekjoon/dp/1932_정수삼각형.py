import sys

input = sys.stdin.readline
n = int(input())
num_list = [list(map(int, input().split(" "))) for i in range(n)]
dp_list = [[0] * i for i in range(1, n)]
dp_list.append(num_list[n - 1])
for i in range(n - 1, 0, -1):
    for j in range(i):
        dp_list[i - 1][j] = num_list[i - 1][j] + max(dp_list[i][j], dp_list[i][j + 1])

print(dp_list[0][0])
