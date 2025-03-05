from collections import defaultdict
def solution(clothes):
    answer = 0
    temp_dict = defaultdict(int)
    for i in clothes:
        temp_dict[i[1]]+=1
    answer=1
    for i in temp_dict.values():
        answer*=i+1
    return answer-1
