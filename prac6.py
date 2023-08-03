# Largest of enterd

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
num3 = int(input("Enter number3 : "))
num4 = int(input("Enter number4 : "))

list = [num1,num2,num3,num4]
list.sort()
print(list[-1])