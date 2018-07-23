try:
	c=0
	n=str(raw_input())
	x=[]
	m=str()
	for i in range (0,len(n)):
		x.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(c!=j):
		t=x[c]
		x[c]=a[c+1]
		x[c+1]=t
		c=c+2
	for i in range (0,len(x)):
		m=m+x[i]
	print m
except:
	print "Invalid"
