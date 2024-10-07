import sys

input = sys.stdin.readline

n = int(input().rstrip())
serial_list = [input().rstrip() for _ in range(n)]

# 리스트 컴프리헨션 사용해도됨
serial_list = sorted(
    serial_list, key=lambda x: [len(x), sum(map(int, filter(str.isdigit, x))), x]
)
for i in serial_list:
    print(i)
