def sum_to(n):
	if n:
		return n + sum_to(n - 1)
	return 0

print(sum_to(3))