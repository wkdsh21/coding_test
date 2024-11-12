import sys

input = sys.stdin.readline

a, b = map(int, input().split())

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

answer_set = a_set - b_set
print(len(answer_set))
print(" ".join(map(str, sorted(list(answer_set)))))
