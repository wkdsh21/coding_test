def solution(citations):
    citations = sorted(citations, reverse=True)
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] >= i + 1:
            return i + 1
    return 0  # for문이 끝나도 return되지않을때
