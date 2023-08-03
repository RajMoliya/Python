# #  Single Inheritance
# class Employee:
#     company = "Facebook"
#     def showDetails(self):
#         print(f"This is {self.company} Employee")

# class Programer(Employee):
#     lang = "Python"
#     def getLang(self):
#         print(f"The language is {self.lang}")
#     def showDetails(self):
#         print(f"This is {self.company} Programer")

# e = Employee()
# p = Programer()
# e.showDetails()
# p.showDetails()
# print(p.company)

# # Multiple Inheritance
# class Employee():
#     company = "Facebook"
#     eCode = 120

# class Freelancer():
#     company = "Fiverr"
#     level = 0
#     def upgrade(self):
#         self.level = self.level +1

# class Programer(Employee,Freelancer):
#     pass

# p = Programer()
# print(p.company)
# p.upgrade()
# print(p.level)

# Multilevel Inheritance
class Person:
    country = "India"
    city = "Jamnagar"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Facebook"
    salary = 500
    def getSalary(self):
        print(f"Salary is : {self.salary}")
    def takeBreath(self):
        print("I am Employee so i am programming")

class Programmer(Employee):
    def getSalary(self):
        print(f"No salary is given to programmers")
    def takeBreath(self):
        print("I am Employee so i am programming++++")

p = Person()
e = Employee()
pr = Programmer()
p.takeBreath()
e.takeBreath()
pr.takeBreath()
print(pr.company)
print(pr.country)


