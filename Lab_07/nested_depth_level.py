def nested_depth_level(lst):
    layer = 1
    for i in lst:
        if isinstance(i, list):
            layer = max(layer, 1 + nested_depth_level(i))
    return layer


# lst = [[1, 2], 3, [4, [5, 6, [7], 8]]]
# lst2 = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
# print(nested_depth_level(lst))
# print(nested_depth_level(lst2))

