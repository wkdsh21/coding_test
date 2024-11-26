from heapq import heappush, heappop


def test1(n, li):
    # 자신의 코드 넣기
    # n(회의의 수),li(회의시간 리스트) 자신의 변수명에맞게 수정

    return answer  # 정답 리턴 (회의의 최대 개수)


def test2(n, lists):
    lists.sort()
    start = lists[0][0]
    end = lists[0][1]
    lists.pop(0)
    answer = 0
    for i in lists:
        if end <= i[0]:
            start = i[0]
            end = i[1]
            answer += 1
        elif i[1] < end:
            start = i[0]
            end = i[1]
    return answer + 1


import random

while True:
    a = []
    one = 0
    two = 0
    for i in range(100):
        N = 10

        # 수열의 값은 1 ≤ a_i ≤ 100,000 사이의 양의 정수로 구성됩니다.
        num_list = []
        for i in range(N):
            temp = random.randint(1, 10)
            num_list.append((temp, temp + random.randint(0, 2)))
        one = test1(N, num_list)
        two = test2(N, num_list)
        if one != two:
            a.append((N, num_list))
    answer = []
    if a and one != two:
        answer = a[0]
        min_val = a[0][0]
        for i in a:
            if min_val > i[0]:
                min_val = i[0]
                answer = i
        print(answer, one, two)
        break
# (n,li) ,자신의 정답, 정답코드의 정답 순으로 출력됨
