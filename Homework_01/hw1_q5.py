# Mingxuan Zhang
# CS-UY 1134

def fibs(n):
	seq = [1, 1]
	yield seq[0]
	yield seq[1]
	for i in range(2, n):
		seq.append(seq[i - 1] + seq[i - 2])
		yield seq[i]

def main():
	for curr in fibs(8):
		print(curr)

# if __name__ == '__main__':
# 	main()