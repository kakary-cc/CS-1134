def nested_sum(lst):
    sum = 0
    for i in lst:
        if isinstance(i, int):
            sum += i
        elif isinstance(i, list):
            sum += nested_sum(i)
    return sum


# lst = [[1, 2], 3, [4, [5, 6, [7], 8]]]

