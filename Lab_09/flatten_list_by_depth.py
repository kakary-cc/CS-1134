from ArrayQueue import *

def flatten_list_by_depth(lst):
	q = ArrayQueue()
	new_lst = []


	while True:
		for elem in lst:
			if isinstance(elem, int):
				q.enqueue(elem)
	return new_lst


print(flatten_list_by_depth([ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9])