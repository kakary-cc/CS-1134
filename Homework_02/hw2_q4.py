def e_approx(n):
	e = 1
	factorial = 1
	for i in range(1, n + 1):
		factorial *= i
		e += 1 / factorial
	return e

def main():
	for n in range(15):
		curr_approx = e_approx(n)
		approx_str = "{:.15f}".format(curr_approx)
		print("n =", n, "Approximation:", approx_str)

# if __name__ == '__main__':
# 	main()