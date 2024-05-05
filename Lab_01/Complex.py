class Complex:
	def __init__(self, a, b):
		self.real = a
		self.complex = b

	def __add__(self, other):
		return Complex(self.real + other.real, self.complex + other.complex)

	def __sub__(self, other):
		return Complex(self.real - other.real, self.complex - other.complex)

	def __mul__(self, other):
		return Complex(self.real * other.complex - self.complex * other.real, self.real * other.complex + self.complex * other.real)

	def __repr__(self):
		if self.complex >= 0:
			return str(self.real) + "+" + str(self.complex) + "i"
		return str(self.real) + "" + str(self.complex) + "i"

# a = Complex(5, 2)
# b = Complex(3, 3)
# print(a * b)