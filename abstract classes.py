# not allow users to create an instance of a Shape Class
# make sure that the methods in Shape class will be implemented in Square class

from abc import ABC, abstractmethod # abc stands for abstract-based classes

class Shape(ABC):
	@abstractmethod                 # abstractmethod decorator: to make following method abstract
	def area(self): pass            # abstract method: method that must be implemented in the subclass

	@abstractmethod
	def perimeter(self):pass

class Square(Shape):
	def __init__(self, side):
		self.__side = side
	def area(self):
		return self.__side * self.__side
	def perimeter(self):
		return 4 * self.__side


square = Square(5)
print(square.area())
print(square.perimeter())









'''
shape = Shape() # with abstract method, object can not be instantiated, the Shape class become effect class(abstract class)
'''