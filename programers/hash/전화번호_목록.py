def solution(phone_book):
    # set자료형은 탐색이 O(1)임
    # 사전순으로 정렬하면 인접한 목록이 접두사가 될 확률이높다
    phone_set = set(phone_book)
    phone_book.sort(key=lambda x: len(x))
    for i in phone_book:
        for j in range(len(phone_book[0]), len(i)):
            if i[:j] in phone_set:
                return False
    return True
