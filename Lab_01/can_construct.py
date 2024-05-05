def can_construct(word, letters):
	lst = [0] * 26
	
	for char in letters:
		lst[ord(char) - 97] += 1 # ord('a') = 97

	for char in word:
		lst[ord(char) - 97] -= 1
		if lst[ord(char) - 97] < 0:
			return False

	return True

# print(can_construct("apples", "applessssss"))