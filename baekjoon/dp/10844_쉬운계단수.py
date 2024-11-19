import sys

input = sys.stdin.readline

n = int(input())

dp_old = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp_new = [0] * 10
for _ in range(n - 1):
    dp_new[0] = dp_old[1]
    for i in range(1, 9):
        dp_new[i] = dp_old[i - 1] + dp_old[i + 1]
    dp_new[9] = dp_old[8]
    dp_old, dp_new = dp_new, dp_old
print(sum(dp_old) % 1000000000)
