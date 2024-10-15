from collections import defaultdict
from collections import deque


def test1(n, k, num_list):

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

    return max_answer


def test2(n, k, num_list):
    max_answer = 1
    s = 0
    num_dict = dict()
    for idx, v in enumerate(num_list):
        if v in num_dict:
            num_dict[v][0] += 1
            num_dict[v][1].append(idx)
        else:
            num_dict[v] = [1, deque([idx])]

        if num_dict[v][0] > k:
            max_answer = max(max_answer, idx - s)
            new_s = num_dict[v][1].popleft() + 1
            for i in num_list[s:new_s]:
                num_dict[i][0] -= 1
            s = new_s
    max_answer = max(max_answer, n - s)
    return max_answer


import random

while True:
    a = []
    for i in range(100):
        N = random.randint(1, 20)  # 1 ≤ N ≤ 200,000
        K = random.randint(1, 100)  # 1 ≤ K ≤ 100

        # 수열의 값은 1 ≤ a_i ≤ 100,000 사이의 양의 정수로 구성됩니다.
        num_list = [random.randint(1, 100) for _ in range(N)]
        if test1(N, K, num_list) != test2(N, K, num_list):
            a.append((N, K, num_list))
    answer = []
    if a:
        answer = a[0]
        min_val = len(a[0][2])
        for i in a:
            if min_val > len(i[2]):
                min_val = len(i[2])
                answer = i
        print(answer)
        break
