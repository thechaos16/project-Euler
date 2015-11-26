>>> def fact(a):
	answer=1
	for i in range(1,a+1):
		answer=answer*i
	return answer

>>> p=fact(100)
>>> while 1:
	dap=dap+p%10
	p=p/10
	if p==0:
		break