import sys

# 역으로 생각하기 답을먼저 정해놓고 이정답이 맞는지 확인 (될때 까지 반복)
input = sys.stdin.readline

k, n = map(int, input().split())
lan_cm = []
for i in range(k):
    lan_cm.append(int(input()))

start = 1
end = max(lan_cm)
answer = None
while start <= end:
    mid = (start + end) // 2
    count = 0
    for lan in lan_cm:
        count += lan // mid
    if count >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
