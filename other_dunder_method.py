class OverLoad:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2): 
        print("Lets Add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("Lets Add") 
        return self.num * num2.num
    
    def __str__(self):  #Prints Object instead of address
        return f"Decimal number : {self.num}"
    def __len__(self):   #Return length
        return 1
    
n1 = OverLoad(4)
print(n1)
print(len(n1))