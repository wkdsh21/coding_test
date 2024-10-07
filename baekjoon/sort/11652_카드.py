import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]
counter = Counter(num_list)
counter = sorted(counter.items(), key=lambda x: [x[1], -x[0]])
# 최빈값만 구하면 되므로 모든데이터를 정렬할 필요는없다
# max_count = max(counter.values())
# result = min([key for key, value in counter.items() if value == max_count])
# 더 짦은시간이 걸림
print(counter[-1][0])
