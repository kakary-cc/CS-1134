def deep_reverse(lst):
    lst.reverse()
    for i in lst:
        if isinstance(i, list):
            deep_reverse(i)


# lst = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
# deep_reverse(lst)
# print(lst)
