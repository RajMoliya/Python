class Employee:
    company = "Not Declared"
    def getSalary(self,signature):
        print(f"Salary of {self.name} working in {self.company} is {self.salary}\n{signature}")

    @staticmethod # When declared no need give self as arg to function
    def greet():
        print("Good Morning, Sir")

    def __init__(self,name,salary,company):
        print("Employee is created")
        self.name = name
        self.salary = salary
        self.company = company

    def getDetail(self):
        print(f"Name of Employee is : {self.name}")
        print(f"Salary of Employee is : {self.salary}")
        print(f"Company of Employee is : {self.company}")
        

e1 = Employee("Raj","500LPA","Facebook")
# e1 = Employee() --> Throws an error as argument defined in constructor is required
e1.getDetail()
