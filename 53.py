a=int(input())
b=0
while(a>0):
    dig=a%10
    b=b+dig
    a=a//10
print(b)
