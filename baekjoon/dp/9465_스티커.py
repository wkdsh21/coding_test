import sys

input = sys.stdin.readline
# n=1일때 n=2일때 n=3일때 이렇게 차근차근 어떻게 해법이 달라지는지 확인후
# dp는 계속 앞으로진행하면서 전의 dp값들을 이용한다는 사실을 잊지말자
# dp 앞쪽에 초기값 넣는것도 필수 dp[0], dp[1]에 값넣고 dp[2]부터 알고리즘 짜기

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] += dp[1][0] + sticker[0][1]
        dp[1][1] += dp[0][0] + sticker[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + sticker[0][i]
            dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + sticker[1][i]

        print(max(dp[0][n - 1], dp[1][n - 1]))
