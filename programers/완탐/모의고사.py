def solution(answers):
    answer = {1: 0, 2: 0, 3: 0}
    for idx_i, v_i in enumerate(
        [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    ):
        for idx_j, v_j in enumerate(answers):
            if v_i[idx_j % len(v_i)] == v_j:
                answer[idx_i + 1] += 1
    sort_answer = sorted(answer.items(), key=lambda x: (-x[1], x[0]))
    return [i[0] for i in sort_answer if sort_answer[0][1] == i[1]]  # map,filter 대체
