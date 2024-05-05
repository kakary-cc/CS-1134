from add_binary import *

class UnsignedBinaryInteger:
	def __init__(self, bin_num_str):
		self.data = bin_num_str

	def __add__(self, other):
		return UnsignedBinaryInteger(add_binary(self.data, other.data)[::-1])

	def decimal(self):
		pass # unfinished

	def __lt__(self, other):
		return int(self.data) < int(other.data)

	def __gt__(self, other):
		return int(self.data) > int(other.data)

	def __eq__(self, other):
		return self.data == other.data

	def is_twos_power(self):
		for i in range(1, len(self.data)):
			if self.data[i] == '1':
				return False
		return True

	def largest_twos_power(self):
		return 2 ** (len(self.data) - 1)

	def __repr__(self):
		return "0b" + self.data

b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')

print('b1: ', b1)
print('b2: ', b2)

b3 = b2 + b1
print('b3: ', b3)

print("\nChecking decimal values:\n")
# print(b1.decimal())
# print(b2.decimal())
# print(b3.decimal())

print("\nChecking comparsions:\n")
print(b1 < b2)
print(b2 < b1)
print(b1 + b2 == b3)

print("\nChecking is_twos_power:\n")
print(b1.is_twos_power())
print(b2.is_twos_power())
print(b3.is_twos_power())

print("\nChecking largest_twos_power:\n")
print(b1.largest_twos_power())
print(b2.largest_twos_power())
print(b3.largest_twos_power())