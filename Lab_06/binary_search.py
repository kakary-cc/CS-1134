def binary_search(lst, low, high, val):
	if low > high:
		return None
	mid = (low + high) // 2
	if val == lst[mid]:
		return mid
	elif lst[mid] > val:
		return binary_search(lst, low, mid - 1, val)
	return binary_search(lst, mid + 1, high, val)

lst = [2, 4, 6, 8, 9, 13, 15, 67]
print(binary_search(lst, 0, len(lst), 2))