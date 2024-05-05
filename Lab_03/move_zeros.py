def move_zeros(num):
	last_zero = 0
	for i in range(len(num)):
		if num[i] != 0:
			num[i], num[last_zero] = num[last_zero], num[i]
			last_zero += 1

lst=[0, 1, 0, 3, 13, 0]
move_zeros(lst)
print(lst)