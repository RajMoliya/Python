# Filter Function 

def greater(n):
    if n>7:
        return True
    else:
        return False

l = [1,2,3,5,8,9,22,46,97,55,75,10]

l7 = lambda n1: n1<7

print(list(filter(greater,l)))
print(list(filter(l7,l)))