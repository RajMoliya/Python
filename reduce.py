# reduce Function 
while(True):
    from functools import reduce

    sum = lambda a,b:a+b

    l = []
    print("Enter 'q' to Quit")
    a = input("Enter a Number : ")
    if a == 'q':
        break
    for i in range(0,int(a)+1):
        l.append(i)

    val = reduce(sum,l)
    print(val)