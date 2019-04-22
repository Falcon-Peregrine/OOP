# aggregation: represents Has-A relationship
# it is a unidirectional association: pass salary object into Employee class, not the other way around
class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return (self.pay*12) + self.bonus

class Employee: # pass an object of salary class in the Employee constructor
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.obj_salary = salary

	def total_salary(self):
		return self.obj_salary.annual_salary()

salary = Salary(15000, 10000)
emp = Employee('Tom', 25, salary)
print(emp.total_salary())