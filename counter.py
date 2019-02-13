class Counter:

	def getValue(self):
		return self._value

	def click(self):
		self._value = self._value + 1

	def reset(self):
		self._value = 0

	def undo(self):
		if self._value > 0:
			self._value = self._value - 1
		else:
			self._value = self._value
