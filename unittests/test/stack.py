class Stack:
	def __init__(self):
		self._values_ = []
	
	def __len__(self):
		return len(self._values_)

	def peek(self):
		return self._values_[-1]

	def push(self, value):
		self._values_.append(value)

	def pop(self):
		return self._values_.pop()
