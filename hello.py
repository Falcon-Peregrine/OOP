'''
class Hello:
	# default argument: name='max'
	def __init__(self, name='max'):pass

h = Hello()
d = Hello('Name')


class Goodbye:
	# multiple arguments: *args
	# keyword arguments(key-value pair): **kwargs
	def __init__(self, *args, **kwargs):pass

value = 5
a = Goodbye()
b = Goodbye('23',34,32, df =value)
'''
class Hello:
	# default argument: name='max'
	def __init__(self, name='max'):
		self.name = name
		
		self.age = 10  # age is not taken from parameter, it is a stactic value
		self.a = 10
		self._b = 20
		self.__c = 30
	def public_method(self):
		print(self.a)
		print(self.__c)
		print('public')
		self.__private_method()
	def __private_method(self):
		print('private')

h = Hello()
hello = Hello('Name')
hello.public_method()
# hello.__private_method()
