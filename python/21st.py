>>> def sof(k):
	summ=0
	for i in range(1,k):
		if k%i==0:
			summ=summ+i
	return summ

>>> def amicable(a,b):
	if sof(a)==b:
		if sof(b)==a:
			return 1
		else:
			return 0
	else:
		return 0

>>> cnt=0
>>> for i in range(1,10001):
	temp=sof(i)
	if amicable(i,temp):
		if i!=temp:
			cnt=cnt+i
			print i

