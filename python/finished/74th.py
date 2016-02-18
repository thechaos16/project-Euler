>>> l=[1,1,2,6]

>>> def fact(n):
	if n<len(l):
		return l[n]
	else:
		p = n*fact(n-1)
		l.append(p)
		return p

>>> def sof(n):
	st = str(n)
	ans=0
	for i in range(len(st)):
		ans = ans+fact(int(st[i]))
	return ans

>>> cnt=0
>>> for i in range(1000000):
	array=[i]
	p = sof(i)
	while 1:
		if p in array:
			break
		array.append(p)
		p = sof(p)
	if len(array)==60:
		print i