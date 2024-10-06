# 10
#    1 100 2 50 60 3 5 6 7 8
# dp 1 1,100 1,2   [1,2,50]   [1,2,50,60]
# 10 2 4 8 2 8 9 3 7 7 7 7
# 10 2 [2,4] [2,4,8] 2 [2,4,8] [2,4,8,9] [2,3] []
# 직접 머릿속으로 테스트케이스에서 결과값을 도출해보기 -> 방법을 일반화 해보기
import sys

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split(" ")))
dp = [0] * n
dp[0] = A[0]
for i in range(1, n):
    max_value = 0
    for j in range(i - 1, -1, -1):
        if A[j] < A[i] and max_value < dp[j]:
            max_value = dp[j]
    dp[i] = max_value + A[i]
print(max(dp))
