def split_parity(lst):
	for i in range(len(lst)):
		if lst[i] % 2 == 0:
			lst.append(lst.pop(i))
			i -= 1

def main():
	lst = [1, 2, 3, 4, 5]
	split_parity(lst)
	print(lst)

# if __name__ == '__main__':
# 	main()