def reverse_vowels(input_str):
	vowels = ['a', 'e', 'i', 'o', 'u']
	list_str = list(input_str)
	vowels_loc = []
	for i in range(len(list_str)):
		if list_str[i] in vowels:
			vowels_loc.append(i)
	for i in range(len(vowels_loc) // 2):
		list_str[vowels_loc[i]], list_str[vowels_loc[-1 - i]] = list_str[vowels_loc[-1 - i]], list_str[vowels_loc[i]]
	return "".join(list_str)

print(reverse_vowels("tandon"))
print(reverse_vowels("ringo"))
print(reverse_vowels("alphabet"))