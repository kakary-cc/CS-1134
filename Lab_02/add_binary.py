def add_binary(bin_num1 = "", bin_num2 = ""):

	if len(bin_num1) > len(bin_num2):
		bin_num1, bin_num2 = bin_num2, bin_num1
		# Makes bin_num2 always the longer one
	len1 = len(bin_num1) - 1
	len2 = len(bin_num2) - 1
	for i in range(0, len2 - len1):
		bin_num1='0' + bin_num1
	result = ""
	flag = False

	for i in range(0, len2 + 1):
		tmp = int(bin_num1[len2 - i]) + int(bin_num2[len2 - i])
		if flag:
			tmp += 1
		if tmp == 2:
			result += '0'
			flag = True
		else:
			result += str(tmp)
			flag = False

	if flag:
		result += '1'
	return result

# print(add_binary("10101", "10101")[::-1])