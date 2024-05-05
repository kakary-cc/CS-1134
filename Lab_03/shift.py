from reverse_list import *

def shift(lst, k):
	reverse_list(lst)
	reverse_list(lst, 0, len(lst) - k - 1)
	reverse_list(lst, len(lst) - k, len(lst) - 1)

# lst = [1, 2, 3, 4, 5, 6]
# shift(lst, 5)
# print(lst)