>>> l = [1,1]


>>> def fibo(n):
	if(len(l)>=n):
		return l[n-1]
	else:
		p = fibo(n-1)+fibo(n-2)
		l.append(p)
		return p

>>> i=50
>>> while 1:
	if(len(str(fibo(i)))==1000):
		print i
	i=i+1