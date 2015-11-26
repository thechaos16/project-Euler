>>> la=[1]
>>> lb=[1]
>>> lc=[1]

>>> def an(n):
	if n<=len(la):
		return la[n-1]
	ans = an(n-1)+8*n-14
	la.append(ans)
	return ans

>>> def bn(n):
	if n<=len(lb):
		return lb[n-1]
	ans = bn(n-1)+8*n-12
	lb.append(ans)
	return ans

>>> def cn(n):
	if n<=len(lc):
		return lc[n-1]
	ans = cn(n-1)+8*n-10
	lc.append(ans)
	return ans

>>> from math import sqrt
>>> def prime(n):
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

>>> cnt=0
>>> i=2

>>> while 1:
	if prime(an(i))==1:
		cnt=cnt+1
	if prime(bn(i))==1:
		cnt=cnt+1
	if prime(cn(i))==1:
		cnt=cnt+1
	deno = 1+4*(i-1)
	if float(cnt)/float(deno)<=0.1:
		print i, cnt, deno
		break
	i=i+1