# # Examole 1
# class AirlineForm:
#     def printData(self):
#         print(f"Name : {self.name}")
#         print(f"AirLine : {self.airline}")

# new_Application = AirlineForm()
# new_Application.name = input("Enter you name : ")
# new_Application.airline = input("Enter your airline : ")
# new_Application.printData()


# Example 2
class Employee:
    company = "Not Declared"
    def getSalary(self,signature):
        print(f"Salary of {self.name} working in {self.company} is {self.salary}\n{signature}")

    @staticmethod # When declared no need give self as arg to function
    def greet():
        print("Good Morning, Sir")

e1 = Employee()
e1.name = "Raj Moliya"
e1.company = "Facebook"
e1.salary = "500LPA"
e1.getSalary("Thanks!") # is == Employee.getSalary(e1)

e2 = Employee()
print(e2.company)

e1.greet()