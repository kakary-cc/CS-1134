def count_lowercase(s, low, high):
    if low > high:
        return 0
    if s[low].islower():
        return count_lowercase(s, low + 1, high) + 1
    else:
        return count_lowercase(s, low + 1, high)

def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    if s[low].islower():
        return not is_number_of_lowercase_even(s, low + 1, high)
    else:
        return is_number_of_lowercase_even(s, low + 1, high)

# s = 'Apple'
# print(count_lowercase(s, 0, len(s) - 1))
# print(is_number_of_lowercase_even(s, 0, len(s) - 1))