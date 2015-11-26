>>> from math import sqrt
>>> pri=[2,3,5]
>>> nonpri=[1,4,6,8]
>>> def prime(n):
	if n in pri:
		return 1
	elif n in nonpri:
		return 0
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			nonpri.append(n)
			return 0
	pri.append(n)
	return 1

>>> def truncate(n):
	a=n
	b=n
	length = len(str(n))
	for i in range(length):
		if prime(a)==0 or prime(b)==0:
			return 0
		a=a/10
		b=b-(b/pow(10,length-i-1))*pow(10,length-i-1)
	return 1

>>> i=10
>>> cnt=[]
>>> while 1:
	if truncate(i)==1:
		cnt.append(i)
	if len(cnt)==11:
		break
	i=i+1