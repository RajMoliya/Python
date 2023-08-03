# while(True):
#     print("Prees 'q' to Quit the Game")
#     a = input("Enter a Number : ")
#     if a =='q':
#         break
    
#     try:
#         a = int(a)
#         if a>6:
#             print("You are right")
#     except Exception as e:
#         print(f"Erorr is : {e}")
    
# print("Thanks for plying this game")

#  Raising a custom Exception
def increment(num):
    try:
        int(num)
        return num +1
    except:
        raise ValueError("Not Valid Input")
a = increment("asd")
print(a)

