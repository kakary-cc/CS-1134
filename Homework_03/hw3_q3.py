def find_duplicates(lst):
    tmp = [0] * len(lst)
    for i in lst:
        tmp[i] += 1
    res = []
    for i in range(len(tmp)):
        if tmp[i] > 1:
            res.append(i)
    return res