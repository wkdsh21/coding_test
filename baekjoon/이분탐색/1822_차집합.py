import sys

input = sys.stdin.readline

a, b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

answer_set = a_set - b_set
print(len(answer_set))
print(" ".join(map(str, sorted(list(answer_set)))))

# 이분탐색은 무조건 정렬이된 리스트에서만 가능
