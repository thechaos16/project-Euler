>>> l=[]
>>> for a in range(2,101):
	for b in range(2,101):
		k=pow(a,b)
		if k in l:
			continue
		l.append(k)

>>> len(l)