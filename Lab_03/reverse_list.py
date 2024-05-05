def reverse_list(lst, low = None, high = None):
	if isinstance(low, int):
		for i in range((high - low + 1) // 2):
			lst[low + i], lst[high - i] = lst[high - i], lst[low + i]
	else:
		for i in range(len(lst) // 2):
			lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

# lst = [1, 2, 3, 4, 5, 6]
# reverse_list(lst, 0, 3)
# print(lst)