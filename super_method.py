# Super Method
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
        super().takeBreath()  #Super Method called
        print("I am Employee so i am programming")

class Programmer(Employee):
    def getSalary(self):
        print(f"No salary is given to programmers")
    def takeBreath(self):
        super().takeBreath()    #Super Method called
        print("I am Employee so i am programming++++")

p = Person()
e = Employee()
pr = Programmer()
p.takeBreath()
e.takeBreath()
pr.takeBreath()
print(pr.company)
print(pr.country)


# Note : It can also run constructor