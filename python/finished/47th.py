def factor(n):
	l=[]
	for i in range(1,n+1):
		if n%i==0:
			l.append(i)
	return l

pri=[2,3,5]

def prime(n):
	if n<2:
		return 0
	if n in pri:
		return 1
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			return 0
	pri.append(n)
	return 1

def primefact(n):
	l=factor(n)
	p=[]
	for i in range(len(l)):
		if prime(l[i])==1:
			p.append(l[i])
	return p

i=646

while 1:
	if len(primefact(i))==4 and len(primefact(i+1))==4 and len(primefact(i+2))==4 and len(primefact(i+3))==4:
		print i
		break
	i=i+1

