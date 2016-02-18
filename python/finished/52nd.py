>>> def perm(a,b):
	if len(str(a))!=len(str(b)):
		return 0
	la = []
	lb = []
	for i in range(len(str(a))):
		la.append(a%10)
		lb.append(b%10)
		a=a/10
		b=b/10
	la.sort()
	lb.sort()
	if la==lb:
		return 1
	return 0


>>> i=10
>>> while 1:
	if perm(i,2*i)==1 and perm(i,3*i)==1 and perm(i,4*i)==1 and perm(i,5*i)==1 and perm(i,6*i)==1:
		print i
		break
	i=i+1