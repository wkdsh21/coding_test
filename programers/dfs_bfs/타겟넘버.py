from itertools import combinations


# 숫자 각각은 +,- "둘중하나를 무조건 선택해야한다" 중복순열(product)사용 ex)[상의1,상의2,상의3], [하의1,하의2,하의3] 옷조합
def solution(numbers, target):
    answer = 0
    numbers_sumed = sum(numbers)
    for i in range(len(numbers) + 1):
        for j in combinations(numbers, i):
            if numbers_sumed - sum(j) * 2 == target:
                answer += 1
    return answer
