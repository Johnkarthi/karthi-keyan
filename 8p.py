try:
	s1=raw_input()
	x=s1.split(' ')
	g=" "
	for i in range(0,len(a)):
			x[i]=x[i].capitalize()
	c=x[0]
	for i in range(1,len(x)):
		c=c+g+x[i]
	print c
except:
	print "Invalid"
