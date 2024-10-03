from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    dp[1].add(N)
    for i in range(1, 8):
        if number in dp[i]:
            return i
        for j in range(1, i + 1):
            for k in dp[j]:
                for l in dp[i + 1 - j]:
                    try:
                        dp[i + 1].add(k + l)
                        dp[i + 1].add(k - l)
                        dp[i + 1].add(k * l)
                        dp[i + 1].add(k // l)
                    except:
                        pass
        dp[i + 1].add(int(str(N) * (i + 1)))
    if number in dp[8]:
        return 8
    else:
        return -1
