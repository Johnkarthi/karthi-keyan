try:
	s1=str(raw_input())
	s2=str(raw_input())
	x=[]
	y=[]
	z=[]
	c=0
	n=len(s1)
	for i in range(0,n):
		if s1[i] in x :
			y.append(i)
			c=i
		else:
			x.append(s1[i])
	for i in range(0,n):
		if(s1[i]==s1[c]):
			z.append(i)
		else: 
			pass
	a=len(c)-1
	while(a!=0):
		i=c[x]
		j=c[x-1]
		if (s2[i]==s2[j]):
			print "true"
		else:
			print "false"
		x=x-1
except:
	print "Invalid"
