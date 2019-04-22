class Parent:
	def __init__(self, name):
		print('Parent__init', name)

class Parent2:
	def __init__(self, name):
		print('Parent2__init', name)

class Child(Parent, Parent2): # multiple inheritance
	def __init__(self):
		print('Child__init')
		super().__init__('name') # super() return a proxy object that allows you to refer to the superclass
		                         # this is like a intantiation

		Parent.__init__(self, 'parent') # when using multiple inheritance, manually address the Name of superclass in order to use method from it
		Parent2.__init__(self, 'Parent2')

child = Child()
print(Child.__mro__)