def list_min(lst, low, high):
    if low == high:
        return lst[-1]
    prev = list_min(lst, low + 1, high)
    if prev < lst[low]:
        return prev
    return lst[low]


# lst = [13, 9, 3, 4, 2]
# print(list_min(lst, 0, len(lst) - 1))