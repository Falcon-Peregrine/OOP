# encapsulation is one of the principle in OOP
class Car:

	def __init__(self, speed, color):
		self.__speed = speed
		self.__color = color

	def set_speed(self, value): # setter for attributes
		self.__speed = value
	def set_color(self, value):
		self.__color = value

	def get_speed(self): # getter for attributes
		return self.__speed
	# def get_color()
	def get_color(self):
		return self.__color


ford  = Car(200, 'red')
honda = Car(250, 'blue')
audi  = Car(300, 'black')

ford.set_speed(500)
ford.__speed = 400  # private variable can not be changed
print(ford.get_speed())

ford.set_color('red')
print(ford.get_color())
