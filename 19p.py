x=int(input())
l=list(1 for i in range(x))
li=[]
for i in range(2,x,1):
    if l[i]==1:
        for j in range(i*i,x,i):
            l[j]=0
        if x%i==0:
            li.append(i)
print(" ".join(str(x) for x in li))
