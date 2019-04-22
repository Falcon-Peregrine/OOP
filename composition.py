# composition: part-of relationship
class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus

	def annual_salary(self):
		return (self.pay*12) + self.bonus

class Employee: # inheritance can not be applied here, because Employee is not Salary and Salary is not Employee
# the Employee Class acts like a container to contain the salary
	def __init__(self, name, age, pay, bonus):
		self.name = name
		self.age = age
		self.obj_salary = Salary(pay, bonus)

	def total_salary(self):
		return self.obj_salary.annual_salary()

emp = Employee('Tom', 25, 15000, 10000)
print(emp.total_salary())
