def split_by_sign(lst, low, high):
    if low == high:
        return
    if lst[low] > 0:
        lst.append(lst.pop(low))
        high -= 1
    else:
        low += 1
    split_by_sign(lst, low, high)


# lst = [4, -5, 2, 3, -1, -6, 7, 9, 0]
# split_by_sign(lst, 0, len(lst) - 1)
# print(lst)
