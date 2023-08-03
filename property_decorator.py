class Employee:
    company = "Facebook"
    salary = 500
    bonus = 50

    @property
    def totalSal(self):
        return self.salary + self.bonus
    
    @totalSal.setter
    def totalSal(self,val):
        self.bonus = val - self.salary
    
e = Employee()
print(e.totalSal)
e.totalSal = 520
print(e.salary)
print(e.bonus)
