import math

def linear_search(lst, val):
	for i in range(len(lst)):
		if lst[i] == val:
			return i

def jump_search_k(lst, val, k = -1):
	if k == -1:
		k = int(math.sqrt(len(lst)))
	if val > lst[-1]:
		return None
	for i in range(k - 1, len(lst), k):
		if val == lst[i]:
			return i
		elif val < lst[i]:
			result = linear_search(lst[i - k + 1 : i], val)
			if result != None:
				return result + i - k + 1
			return None
	if len(lst) % k:
		result = linear_search(lst[len(lst) - (len(lst) % k) : len(lst)], val)
		if result != None:
			return len(lst) - len(lst) % k + result
	return None

def main():
	lst = [-1111, -818, -646, -50, -25, -3, 0, 1, 2, 11, 33, 45, 46, 51, 58, 72, 74, 75, 99, 110, 120, 121, 345, 400, 500, 999, 1000, 1114, 1134, 4444, 10010, 500000, 999999]

	#Testing k
	for i in range(1, len(lst)):
		# print("i:",i)
		print("TESTING VALUES IN LIST:", "k = ", i, "\n")

		for val in lst:
			if jump_search_k(lst, val, i) is None:
				print(val, "FAILED - DID NOT FIND")
	print("TEST k COMPLETED")

	#Testing sqrt
	print("\nTESTING VALUES IN LIST: k = sqrt(n) \n")
	for val in lst:
		if jump_search_k(lst, val) is None:
			print(val, "FAILED - DID NOT FIND")
	print("TEST sqrt COMPLETED")

if __name__ == '__main__':
	main()

# Worst case time complexity for 4(a): O(n)
# for 4(b): O(sqrt(n))