xx1,y1=map(int,input().split(' '))
if xx1 > y1:
    smaller = y1
else:
    smaller = xx1
for i in range(1, smaller+1):
    if((xx1 % i == 0) and (y1 % i == 0)):gcd1 = i
print(gcd1)
