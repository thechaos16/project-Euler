>>> def prime(n):
	for i in range(2,n/2+1):
		if(n%i==0):
			return 0
	return 1

>>> def square2(i):
	return i*i*2

>>> while 1:
	check=0
	p = 2*i+1
	if(prime(p)==0):
		j=1
		while 1:
			if(square2(j)>p):
				break
			if(prime(p-square2(j))==1):
				check=1
				break
			j=j+1
		if(check==0):
			print p
			break
	i=i+1