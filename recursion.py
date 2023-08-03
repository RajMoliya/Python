# #Calculate factorila of number with function

# def fac_cal(num):
#     factorial =1
#     for i in range(1,num+1):
#         factorial = factorial*i

#     return print(f"Factorial of {num} is {factorial}")
 
# num = int(input("Enter a Number to find factorial : "))
# fac_cal(num)


def fac_recursive(n):
        if n==0 or n==1:
             return 1
        else:
             return n*fac_recursive(n-1)

a = int(input("Enter a Number to find factorial : "))     
f = fac_recursive(a)
print(f"Factorial of {a} is {f}")