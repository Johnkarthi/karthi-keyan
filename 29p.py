import math
i,k =input().split()
i=int(i)
k=int(k)
print(type(i))
count=0
for q in range(i,k):
  if int(math.sqrt(q))**2==q:
      count=count+1
print(count) 
