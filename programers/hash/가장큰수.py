from functools import cmp_to_key


# 복잡한정렬은 cmp_to_key를 사용하여 sorted함수사용  O(n~nlogn)
def solution(numbers):
    def cmp(a, b):
        if a + b < b + a:
            return -1
        else:
            return 0

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(cmp), reverse=True)
    return str(int("".join(numbers)))
