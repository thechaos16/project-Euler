>>> def fraction(a,b):
	if(a<10 or a>=100):
		return 0
	if(b<10 or b>=100):
		return 0
	if(a<=b):
		return 0
	sample = float(b)/float(a)
	k = a%10
	if(k==0):
		k=1000000000000
	temp = [float(b/10)/float(a/10), float(b/10)/float(k), float(b%10)/float(a/10), float(b%10)/float(k)]
	for i in range(4):
		if(sample==temp[i]):
			return 1
	return 0


>>> for i in range(10,99):
	for j in range(i+1,100):
		if(fraction(j,i)==1):
			print i, j