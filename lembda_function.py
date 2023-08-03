# Lambda function 

# def func(a):
#     return a+5

    #   or 

func = lambda a:a+5
square = lambda a:a*a
sum = lambda a,b,c:a+b+c

num = int(input("Enter a Number : "))
print(func(num))
print(square(3))
print(sum(1,5,7))