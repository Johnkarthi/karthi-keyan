x=[]
b=int(input("Enter number of elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    x.append(c)
x.sort()
print("Largest element is:",x[b-1])
