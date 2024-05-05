# Mingxuan Zhang
# CS-UY 1134

import copy

class Vector:
	def __init__(self, d):
		if isinstance(d, list):
			self.coords = copy.copy(d)
		else:
			self.coords = [0] * d

	def __len__(self):
		return len(self.coords)

	def __getitem__(self, j):
		return self.coords[j]

	def __setitem__(self, j, val):
		self.coords[j] = val

	def __add__(self, other):
		if (len(self) != len(other)):
			raise ValueError("dimensions must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __sub__(self, other):
		if (len(self) != len(other)):
			raise ValueError("dimensions must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] - other[j]
		return result

	def __neg__(self):
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] * -1
		return result

	def __mul__(self, val):
		scalar_result = Vector(len(self))
		dot_result = 0
		if isinstance(val, int):
			for j in range(len(self)):
				scalar_result[j] = self[j] * val
			return scalar_result
		
		for j in range(len(self)):
			dot_result += self[j] * val[j]
		return dot_result

	def __rmul__(self, val):
		return self * val

	def __eq__(self, other):
		return self.coords == other.coords

	def __ne__(self, other):
		return not (self == other)

	def __str__(self):
		return '<' + str(self.coords)[1:-1] + '>'

	def __repr__(self):
		return str(self)

