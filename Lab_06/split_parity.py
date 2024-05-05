def split_parity(lst, low, high):
	if low == high:
		return
	if lst[low] % 2:
		lst.append(lst.pop(low))
		high -= 1
	else:
		low += 1
	split_parity(lst, low, high)

lst = [4, -5, 2, 3, -1, -6, 7, 9, 0]
split_parity(lst, 0, len(lst) - 1)
print(lst)