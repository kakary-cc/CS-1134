# Mingxuan Zhang
# CS-UY 1134

a = [10 ** i for i in range(6)]
# print(a)

b = [2 * i for i in range(10)]
b = [sum(b[0 : i + 1]) for i in range(10)]
# print(b)

c = [chr(ord('a') + i) for i in range(26)]
# print(c)