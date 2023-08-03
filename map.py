def square(a):
    return a*a

l= [1,2,3]
l1 = []

# Method 1
for item in l:
    l1.append(square(item))

print(l)
print(l1)

# Method 2 using map 
print(list(map(square,l)))
