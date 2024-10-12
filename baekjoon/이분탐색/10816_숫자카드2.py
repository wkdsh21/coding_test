import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
n_list = [int(i) for i in input().split()]
m = int(input())
m_list = [int(i) for i in input().split()]

n_counter = Counter(n_list)
answer = [n_counter[i] if i in n_counter else 0 for i in m_list]
for i in answer:
    print(i, end=" ")
