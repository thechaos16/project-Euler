>>> def fact(n):
	l = []
	for i in range(1,n):
		if(n%i==0):
			l.append(i)
	return l

>>> def abundant(n):
	l = fact(n)
	sum=0
	for i in range(len(l)):
		sum = sum+l[i]
	if(sum>n):
		return 1
	else:
		return 0

>>> def twoab(n):
	check = 0
	for i in range(1,n/2+1):
		if(abundant(i)==1 and abundant(n-i)==1):
			check = 1
			return check
	return check

>>> ans=0
>>> for i in range(1,28123):
	if(twoab(i)==0):
		ans = ans+i