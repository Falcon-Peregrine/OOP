# Class: blueprint 体
class Car:
	# when the isntance is created, __init__ is called
	# server as a contructor of the class, initialize attributes or functions
	# self refers to the current Object
	def __init__(self, speed, color): #用
		self.speed = speed
		self.color = color
		# print(speed)
		# print(color)






# Object: the instance of a class, containing data and method(function)
ford  = Car(200, 'red') # 相
honda = Car(250, 'blue')
audi  = Car(300, 'black')

print(ford.speed)
print(honda.color)


'''
# Atrribute(variables which holds data):
ford.speed = 200
honda.speed = 220
audi.speed = 250
ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'




# Update Attributes:
ford.speed = 300
ford.color = 'blue'
print(ford.speed)
print(ford.color)
'''