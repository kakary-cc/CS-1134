def is_palindrome(input_str, low, high):
	if low >= high:
		return True
	if input_str[low] != input_str[high]:
		return False
	return is_palindrome(input_str, low + 1, high - 1)

print(is_palindrome("racecar", 0, 6))
print(is_palindrome("racecar", 1, 5))
print(is_palindrome("racecar", 1, 3))
