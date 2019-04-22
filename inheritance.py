class Polygon:
	__width = None
	__height = None
	
	def set_values(self, width, height):
		self.__width = width
		self.__height = height
	def get_width(self):
		return self.__width
	def get_height(self):
		return self.__height
	

class Rectangle(Polygon): # all the public member variables and methods are accessible from the subclass from the superclass
	def area(self):
		return self.get_width() * self.get_height()



class Triangle(Polygon):
	def area(self):
		return self.get_width() * self.get_height() / 2


rect = Rectangle()
tri = Triangle()

rect.set_values(50, 40)
tri.set_values(50, 40)

print(rect.area())
print(tri.area())
