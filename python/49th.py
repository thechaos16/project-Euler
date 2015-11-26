>>> def prime(n):
	for i in range(2,n/2+1):
		if(n%i==0):
			return 1
	return 0


>>> def permu(a,b):
	la=[]
	lb=[]
	for i in range(4):
		la.append(str(a%10))
		lb.append(str(b%10))
		a=a/10
		b=b/10
	la.sort()
	lb.sort()
	if(la==lb):
		return 0
	return 1


>>> for i in range(1000,10000):
	if(prime(i)==0):
		for j in range(i+1,10000):
			if(permu(i,j)==0):
				if(prime(j)==0 and j+j-i<10000):
					if(permu(i,j+j-i)==0 and prime(j+j-i)==0):
						print i, j, j+j-i