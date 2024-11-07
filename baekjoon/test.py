from bisect import bisect_left, bisect_right

a = [1, 3, 4]
num = 2
print(bisect_right(a, num))
print(bisect_left(a, num))
