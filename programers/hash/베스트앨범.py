def solution(genres, plays):
    answer = []
    dicts = dict()
    for i, (j, k) in enumerate(zip(genres, plays)):
        if j not in dicts:
            dicts[j] = [0]
        dicts[j][0] += k
        dicts[j].append([i, k])
    for i in sorted(dicts.items(), key=lambda x: -x[1][0]):
        li = sorted(i[1][1:], key=lambda x: -x[1])[:2]
        for j in li:
            answer.append(j[0])
    return answer
