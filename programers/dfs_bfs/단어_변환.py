from collections import Counter
from collections import deque


# solution("hit", "cog", ["oht", "dot", "dog", "lot", "log", "cog"]) 이렇게 "oht" 같은게있으면 아래는 틀린 코드임
def solution(begin, target, words):
    if target not in words:
        return 0
    deq = deque()
    deq.append((begin, 0))
    while deq:
        temp_word, d = deq.popleft()
        # 중복값이 계속 들어가긴하지만 BFS특성상 무한루프를 돌진않는다(target을 찾으면 종료된다)
        if temp_word == target:
            return d
        for i in words:
            # sum([1 for a,b in zip(temp_word,i) if a!=b]) == 1 이렇게 counter 없이 쓸수있다
            count_val = tuple((Counter(temp_word) - Counter(i)).values())
            if len(count_val) == 1 and count_val[0] == 1:
                deq.append((i, d + 1))
                print(i)
