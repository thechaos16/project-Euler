>>> def palint(n):
	cnt=0
	a=list(str(n))
	b=list(str(n))
	for i in range(len(str(n))-1):
		if a.pop()!=b.pop(0):
			cnt=1
			break
	if cnt==0:
		return 1
	else:
		return 0

	
>>> def palinb(n):
	cnt=0
	a=list(n)
	b=list(n)
	for i in range(len(n)-1):
		if a.pop()!=b.pop(0):
			cnt=1
			break
	if cnt==0:
		return 1
	else:
		return 0

>>> def binary(n):
	ans=''
	while 1:
		ans=str(n%2)+ans
		n=n/2
		if(n==0):
			break
	return ans

>>> sum=0		
>>> for i in range(1000000):
	if palint(i)==1 and palinb(binary(i)):
		sum=sum+i