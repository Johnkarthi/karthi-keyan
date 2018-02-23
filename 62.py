a = 0
b=raw_input()
d=0
c=list(str(b))
for a in range(0,len(c)):
    if(c[a]=="0" or c[a]=="1"):
        d=d+1
if(d==len(c)):
  print("Yes")
else:
  print("no")
