>>> def sod(a):
	value=0
	for i in range(len(str(a))):
		value=value+a%10
		a=a/10
	return value

>>> ans=0
>>> for a in range(1,100):
	for b in range(100):
		ans = max(ans,sod(pow(a,b)))