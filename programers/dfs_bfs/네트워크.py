from collections import deque


def solution(n, computers):
    answer = 0
    deq = deque()
    visit = [0] * n
    deq.append(0)
    while visit.count(0) != 0:
        while deq:
            com = deq.popleft()
            visit[com] = 1
            for idx, v in enumerate(computers[com]):
                if v == 1 and visit[idx] == 0:
                    deq.append(idx)
        deq.append("".join(str(i) for i in visit).find("0"))
        answer += 1
    return answer
