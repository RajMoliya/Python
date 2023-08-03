# # Calculate Percentage
# def percent(marks):
#     return ((sum(marks)/400)*100)

# a = int(input("Enter Mareks Of Subject A : "))
# b = int(input("Enter Mareks Of Subject B : "))
# c = int(input("Enter Mareks Of Subject C : "))
# d = int(input("Enter Mareks Of Subject D : "))
# marks1 = [a,b,c,d]
# percent = percent(marks1)
# print(percent)



# # Greek bot
# def greet(name = "Stranger"): #Default value in case of missing argumrnt
#     print("Good Day,",name)

# greet("Raj")
# greet()

# # Sum of two numbers
# def sum(num1,num2):
#     return (print(f"Sum of {num1} + {num2} = {num1+num2}"))

# sum(5,4)

# remove given string and strip
def edit_str(string,word):
        newStr = string.replace(word,"")
        return newStr.strip()

string = "      Hello My name is Raj     "
s = edit_str(string,"Hello")
print(s)
