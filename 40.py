x=int(input("Enter the Number"))
n1 = 0
n2 = 1
count = 0
l=[]
if x == 1:
    l.append(n1)
    print(l)
else:
    while count < x:
        l.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print(" ".join(str(x) for x in l))
