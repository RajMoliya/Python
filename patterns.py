# # Printing Patterns
#         # *
#         # **
#         # ***
#         # ****
# n = int(input("Eneter no. of stars"))
# j = 0
# for i in range(1,n+1):
#     print("*"*i)


# # Printing Pattern
# #   *  
# #  ***
# # *****
# a = int(input("Eneter no. of Lines"))
# for i in range(0,a):
#     print(" "*(a-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(" "*(a-i-1))


# Printing Pattern
#   *  
#  ***
# *****
#  ***
#   * 
# a = int(input("Eneter no. of Lines"))
a =7
for i in range(0,a):
    print(" "*(a-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(a-i-1))
for i in range(a,0,-1):
    print(" "*(a-i+1),end="")
    print("*"*(2*(i-1)-1),end="")
    print(" "*(a-i+1))