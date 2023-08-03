a = [1,5,7,10,22,100,24,12,35]
b = []
c = []
for item in a:
    if item%2==0:
        b.append(item)
    else:
        c.append(item)
print(b)
print(c)

# with list comprehension
print("List Comprehension")
c = [i for i in a if i%2==0]
print(c)
d = [i for i in a if i%2!=0]
print(d)