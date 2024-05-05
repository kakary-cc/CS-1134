import copy

class Polynomial:
	def __init__(self, lst):
		self.data = copy.copy(lst)

	def __add__(self, other):
		if len(self.data) > len(other.data):
			sum_data = copy.copy(self.data)
			for i in range(len(other.data)):
				sum_data[i] += other.data[i]
		else:
			sum_data = copy.copy(other.data)
			for i in range(len(self.data)):
				sum_data[i] += self.data[i]
		return Polynomial(sum_data)

	def __call__(self, num):
		evaluation = 0
		for i in range(len(self.data)):
			evaluation += self.data[i] * (num) ** i
		return evaluation

# poly1 = Polynomial([3, 7, 0, -9, 2])
# poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])

# poly3 = poly1 + poly2
# print(poly3.data)

# val1 = poly1(1)
# print(val1)
# val2 = poly2(1)
# print(val2)
# val3 = poly3(1)
# print(val3)