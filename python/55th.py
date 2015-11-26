from collections import deque

def palin(n):
	a=[]
	b=deque([])
	for i in range(len(str(n))):
		a.append(int(str(n)[i]))
		b.append(int(str(n)[i]))
	for i in range(len(a)):
		if a.pop()!=b.popleft():
			return 0
	return 1

def reverse(n):
	a=0
	l = len(str(n))
	for i in range(l):
		a=a+int(str(n)[i])*pow(10,i)
	return a

ans=0

for i in range(10000):
	cnt=0
	check=0
	k = i+reverse(i)
	while cnt<=50:
		if palin(k)==1:
			check=1
			break
		k = k+reverse(k)
		cnt=cnt+1
	if check==0:
		ans=ans+1
