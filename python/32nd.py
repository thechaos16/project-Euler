check=['1','2','3','4','5','6','7','8','9']

def pandi(n):
	if len(n)!=9:
		return 0
	l=[]
	for i in range(9):
		l.append(n[i])
	l.sort()
	if l==check:
		return 1
	return 0

from math import sqrt

sum=0

cnt=[]

for i in range(2,9999):
	for j in range(i,9999):
		k = i*j
		forward=str(i)+str(j)+str(k)
		if pandi(forward)==1:
			if k in cnt:
				continue
			cnt.append(k)
			sum=sum+k