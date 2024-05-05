import random
word_lst = ["pokemon", "apple", "bee"]

def create_permutation(n):
	lst = []
	while len(lst) < n:
		tmp = random.randint(0, n - 1)
		if tmp not in lst:
			lst.append(tmp)
	return lst

def scramble_word(word):
	rand_lst = create_permutation(len(word))
	scrambled = ""
	for i in range(0, len(word)):
		scrambled += word[rand_lst[i]]
	return scrambled

random_word = word_lst[random.randint(0, len(word_lst) - 1)]
print("Unscramble the word:  " + scramble_word(random_word))
for i in range(1, 4):
	input_word = input("Try #" + str(i) + ": ")
	if input_word == random_word:
		print("Yay, you got it!")
		break
	else:
		print("Wrong!")