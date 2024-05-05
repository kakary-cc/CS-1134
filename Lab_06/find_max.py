"""
Runtime: T(n) = O(n^2)
"""

def find_max(lst, low, high):
	if low == high:
		return lst[-1]
	prev = find_max(lst, low + 1, high)
	if prev > lst[low]:
		return prev
	return lst[low]

lst = [13, 9, 3, 4, 2]
print(find_max(lst, 0, len(lst) - 1))