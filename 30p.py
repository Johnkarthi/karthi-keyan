lis1,lis2,kk=input().split(' ')
kk=int(kk)
c=0
for i in range(len(lis1)):
    if lis1[i]!=lis2[i]:
        c+=1
if c==k1:print("yes")
else:print("no")
