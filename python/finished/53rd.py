>>> store = {1:1, 2:1}

>>> def fact(n):
	if n in store:
		return store[n]
	else:
		p=n*fact(n-1)
		store[n] = p
		return p

>>> def combi(n, r):
	if r==0 or r==n:
		return 1
	ans = fact(n)/(fact(r)*fact(n-r))
	return ans

>>> cntall=0
>>> for i in range(1,101):
	cnt=0
	for j in range(i/2+1):
		if combi(i,j)>=1000000:
			if i%2==0 and j==i/2:
				cnt = cnt+1
			else:
				cnt = cnt+2
	cntall = cntall+cnt