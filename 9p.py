try:
	count=0
	x=int(raw_input())
	for i in range (1,x+1):
		c=0
		for j in range (1,x+1):
			if (i%j==0):
				c=c+1
			else :
				pass
		if(c==2):
			count=count+1
	print count
except:
	print "Invalid"
