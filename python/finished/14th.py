for i in range(1,1000000):
	j=i
	while 1:
		cnt = cnt+1
		if i==1:
			break
		elif i%2==0:
			i=i/2
		else:
			i=3*i+1
	if cnt>cntmax:
		cntmax = cnt
		answer=j
	cnt=0