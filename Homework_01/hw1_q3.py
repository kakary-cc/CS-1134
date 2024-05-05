# Mingxuan Zhang
# CS-UY 1134

def a(n):
	sum = 0
	for i in range(1, n):
		sum += i ** 2
	return sum
# print(a(5))

# n = 5
b = sum([i ** 2 for i in range(1, n)])
# print(b)

def c(n):
	sum = 0
	for i in range(1, n):
			if i % 2:
				sum += i ** 2
	return sum
# print(c(5))

# n = 5
d = sum([i ** 2 for i in range(1, n) if i % 2])
# print(d)