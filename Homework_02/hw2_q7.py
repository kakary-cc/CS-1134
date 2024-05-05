def findChange(lst01):
	if len(lst01) < 3:
		return len(lst01) - 1
	left = 0
	right = len(lst01) - 1
	while left <= right:
		mid = (left + right) // 2
		if lst01[mid] > lst01[mid - 1]:
			return mid
		elif lst01[mid] == 1 & lst01[mid - 1] == 1:
			right = mid - 1
		elif lst01[mid] == 0 & lst01[mid - 1] == 0:
			left = mid + 1
	return 0

def main():
	lst = [0, 0, 0, 0, 1, 1, 1, 1]
	print(findChange(lst))

# if __name__ == '__main__':
# 	main()