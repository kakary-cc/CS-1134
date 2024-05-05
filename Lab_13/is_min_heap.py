def is_min_heap(lst):

	def node_fit_rule(lst, ind):
		if ind >= len(lst) // 2:
			return True
		if lst[ind * 2] < lst[ind] or lst[ind * 2 + 1] < lst[ind]:
			return False
		return node_fit_rule(lst, ind * 2) and node_fit_rule(lst, ind * 2 + 1)

	return node_fit_rule(lst, 1)


print(is_min_heap([None, 4, 50, 7, 55, 90, 87, None]))