from itertools import combinations_with_replacement  # 중복 조합


def solution(sizes):
    answer = set()
    lists = list(set([i[0] for i in sizes] + [i[1] for i in sizes]))
    for i in combinations_with_replacement(lists, 2):
        check = 0
        for j in sizes:
            if j[0] > i[0] or j[1] > i[1]:
                if j[0] > i[1] or j[1] > i[0]:
                    check = 1
                    break
        if check == 0:
            answer.add(i[0] * i[1])
    return min(answer)
