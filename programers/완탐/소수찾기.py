from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set((0, 1))
    answer = len(a)
    for i in a:
        for j in range(2, i):
            if i % j == 0:
                answer -= 1
                break
    return answer
