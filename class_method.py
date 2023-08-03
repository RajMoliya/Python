class Employee:
    salary = 100

    @classmethod
    def changSal(cls,newsalary):
        cls.salary = newsalary
    
    # def changSal(self,newsalary):  # Aleternate Code
    #     self.__class__.salary = newsalary

e = Employee()
print(e.salary)
e.changSal(555)
print(e.salary)
print(Employee.salary)