x1,k1=map(int,input().split(' '))
l1=list(map(int,input().split(' ')))
k1=list(input().split(' '))
y1=[]
for i in range(len(k)):
    l1.append(i)
    m1.append(max(l1))
    l1.remove(i)
print(" ".join(str(x) for x in y1))
