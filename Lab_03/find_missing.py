"""
a. O(n^2) 
"""

# def find_missing(lst):
# 	if lst[0] == 1:
# 		return 0
# 	elif lst[-1] - 1 != lst[-2]:
# 		return lst[len(lst) - 1] - 1
# 	elif (lst[0] + lst[-1]) * len(lst) / 2 == sum(lst):
# 		return lst[-1] + 1
# 	else:
# 		return int((lst[0] + lst[-1]) * (len(lst) + 1) / 2 - sum(lst))

def find_missing(lst):
	bucket = [False] * (len(lst) + 1)
	for i in lst:
		bucket[i] = True
	for i in range(len(bucket) - 1):
		if not bucket[i]:
			return i
	return len(bucket) - 1

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(find_missing(lst))
lst = [0, 1, 2, 3, 4, 6, 7, 8]
print(find_missing(lst))
lst = [0, 1, 2, 3, 4, 6, 7, 8, 9]
print(find_missing(lst))
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_missing(lst))

lst = [8, 6, 0, 4, 3, 5, 1, 2]
print(find_missing(lst))