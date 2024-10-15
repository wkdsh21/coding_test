import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
num_list = list(map(int, input().split()))
max_answer = 0
s = 0
num_count = defaultdict(int)

for e in range(n):
    num_count[num_list[e]] += 1

    # 같은 숫자가 K개를 초과하는 경우
    while num_count[num_list[e]] > k:
        num_count[num_list[s]] -= 1
        s += 1

    # 최장 길이 갱신
    max_answer = max(max_answer, e - s + 1)

print(max_answer)
