# Mingxuan Zhang
# CS-UY 1134

def shift(lst, k, dir = "left"):
	if dir == "left":
		for i in range(k):
			lst.append(lst.pop(0))
	elif dir == "right":
		for i in range(k):
			lst.insert(0, lst.pop(len(lst) - 1))

def main():
	lst = [1, 2, 3, 4, 5, 6]
	shift(lst, 2, "right")
	print(lst)

# if __name__ == '__main__':
# 	main()