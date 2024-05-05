def remove_all(lst, val):
    count = 0
    i = 0
    while i < len(lst):
        try:
            lst[i] = lst[i + count]
        except IndexError:
            lst[i] = None
        if lst[i] == val:
            count += 1
        else:
            i += 1
    for i in range(count):
        lst.pop()