from math import sqrt

def factors(num):
	lst = []
	for i in range(1, int(sqrt(num)) + 1):
		if num % i == 0:
			lst.append(i)
			yield i
	if lst[-1] == sqrt(num):
		lst.pop()
	for i in reversed(lst):
		yield int(num / i)

def main():
	for curr_factor in factors(100):
		print(curr_factor)

if __name__ == '__main__':
	main()