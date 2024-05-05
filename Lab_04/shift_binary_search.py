def binary_search(srt_lst, val):
  left = 0
  right = len(srt_lst) - 1
  ind = None
  found = False
  while (found == False) and (left <= right):
    mid = (left + right) // 2
    if srt_lst[mid] == val:
      ind = mid
      found = True
    elif val < srt_lst[mid]:
      right = mid - 1
    elif val > srt_lst[mid]:
      left = mid + 1
  return ind

def search_pivot(lst):
	return 3

def shift_binary_search(lst, val):
	pivot = search_pivot(lst)
	result = binary_search(lst[0: pivot], val)
	if result != None:
		return result
	result = binary_search(lst[pivot: len(lst)], val)
	if result != None:
		return result + pivot
	return None

print(shift_binary_search([15, 20, 21, 1, 3, 6, 7, 10, 12, 14], 3))
# NOT FINISHED