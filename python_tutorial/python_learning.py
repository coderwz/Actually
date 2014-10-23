class Peterson:

	def __init__(self, name):
		self.name=name

	def say_hi(self):
		print('Hello, my name is'),self.name

p=Peterson('Swaroop')
p.say_hi()