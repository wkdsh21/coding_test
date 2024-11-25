import sys

input = sys.stdin.readline
num_list = [True] * 1000001
num_list[0], num_list[1] = False, False
# 2의배수 다 False
for i in range(2 * 2, 1000001, 2):
    num_list[i] = False
# 아리스테네?의 체 이용
for i in range(1, 1000001, 2):
    if num_list[i]:
        for j in range(i * 2, 1000001, i):
            num_list[j] = False
# 두수가 모두 소수고 왼쪽값은 제일작은값에서 점점 커지므로 제일먼저 해당하는 조합이 b-a가 제일큰조합임
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, n):
        if num_list[i] and num_list[n - i]:
            print(f"{n} = {i} + {n-i}")
            break
