def solution(participant: list[str], completion: list[str]) -> str:
    # collections.Counter 사용시 더 간결함
    answer = ""
    set_part = set(participant)
    dicts = dict(zip(set_part, [0] * len(set_part)))
    for i in participant:
        dicts[i] += 1
    for i in completion:
        dicts[i] -= 1
    for k, v in dicts.items():
        if v == 1:
            answer = k
            break
    return answer
