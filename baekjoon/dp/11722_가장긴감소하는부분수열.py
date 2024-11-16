import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
dp = [0] * n

for idx, num in enumerate(num_list):
    max_length = 0
    for idx2, num2 in enumerate(num_list[:idx]):
        if num2 > num and max_length < dp[idx2]:
            max_length = dp[idx2]
    dp[idx] = max_length + 1

print(max(dp))
