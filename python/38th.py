>>> def pandigital(n):
	cnt=0
	radix=0
	no=1
	p=''
	while 1:
		radix=radix+len(str(n*no))
		p=p+str(n*no)
		no=no+1
		if(radix>=9):
			break
	if(radix!=9):
		return 0, p
	for i in range(1,10):
		if str(i) in list(p):
			cnt=cnt+1
	if cnt==9:
		return 1,p
	else:
		return 0,p

>>> for i in range(1,9999):
	if pandigital(i)[0]==1:
		L=L+[pandigital(i)[1]]