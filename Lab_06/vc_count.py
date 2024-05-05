def vc_count(word, low, high):
	if low > high:
		return (0, 0)
	vowel, constant = vc_count(word, low + 1, high)
	vowel_char = ['a', 'i', 'u', 'e', 'o']
	if word[low].lower() in vowel_char:
		vowel += 1
	else:
		constant += 1
	return (vowel, constant)

word = "NYUTandonEngineering"
print(vc_count(word, 0, len(word) - 1))