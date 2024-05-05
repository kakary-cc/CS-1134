def product_evens(n):
	if n == 0:
		return 1
	elif n % 2:
		n -= 1
	print(n)
	return n * product_evens(n - 2)

print(product_evens(2))