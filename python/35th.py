>>> def prime(n):
	check=0
	for i in range(2,n/2+1):
		if(n%i==0):
			check = 1
			return check
	return check


>>> def circle(n):
	p = len(str(n))
	check = 0
	k=n
	for i in range(p):
		if(prime(k)==1):
			check = 1
			return check
		temp = k%10
		k = k/10 + temp*pow(10,p-1)
	return check

>>> cnt=0


>>> for i in range(2,1000000):
	if(circle(i)==0):
		cnt=cnt+1