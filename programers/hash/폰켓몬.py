def solution(nums: list[int]) -> int:
    # min함수로 대상값이 기준값을 넘으면 대상값 대신 기준값을 리턴하도록 할수있음
    type_len = len(set(nums))
    select_len = len(nums) // 2
    return min(type_len, select_len)
