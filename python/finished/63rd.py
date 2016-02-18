>>> def length(n,a):
	return len(str(pow(n,a)))


>>> for i in range(1,10):
	j=1
	while 1:
		if(j==length(i,j)):
			cnt=cnt+1
		elif(j>length(i,j)):
			break
		j=j+1
	print cnt