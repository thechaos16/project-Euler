>>> def prime(n):
	if(n<1):
		return 0
	for i in range(2,n/2+1):
		if(n%i==0):
			return 0
	return 1


>>> def formula(a,b):
	i=0
	while 1:
		ans = i*i+a*i+b
		if(prime(ans)==0):
			break
		i=i+1
	return i

>>> maximum=0
>>> dap=0
>>> for a in range(-999,1000):
	for b in range(-999,1000):
		if(prime(b)==1):
			if(formula(a,b)>maximum):
				maximum=formula(a,b)
				dap = a*b