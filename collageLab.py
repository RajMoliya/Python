# # Print Hello World
# print("Hello, World")

# # Add 2 Numbers
# x = 5
# y = 7
# z = x + y
# print(z)

# # Add 2 no. input by users
# num1 = int(input("Enter number1\n"))
# num2 = int(input("Enter number2\n"))
# num3 = num1 + num2
# print(num3)

# # Swap 2 no. input by users
# num1 = int(input("Enter number1\n"))
# num2 = int(input("Enter number2\n"))
# print(num1)
# print(num2)
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1)
# print(num2)


# # GDC of 2 Numbers
# num1 = int(input("Enter number1\n"))
# num2 = int(input("Enter number2\n"))
# if num1>num2:
#     small = num2
# else:
#     small = num1
# for a in range(1,small+1):
#     if(num1%a==0 and num2%a==0):
#         gdc = a
# print("Gdc of",num1,"and",num2,"is : ",gdc)

    

# # Input 3 numbers and print smallest and largest
# num1 = int(input("Enter number1\n"))
# num2 = int(input("Enter number2\n"))
# num3 = int(input("Enter number3\n"))
# list = [num1,num2,num3]
# list.sort()
# print("greatest no. is",list[2])
# print("smallest no. is",list[0])

# Odd & Even 
a = int(input('Enter a Number : '))
if a%2==0:
    print(f"{a} is Even Number")
else:
    print(f"{a} is Odd Number")

# print 0 to n using while loop 
a = int(input('Enter a Number : '))
i = a
while i>=0:
    print(i)
    i-=1

# Print Odd numbers in range 
a = int(input('Enter a initial Number : '))
b = int(input('Enter a final Number : '))
for i in range(a+1,b):
    if i%2!=0:
        print(i)












