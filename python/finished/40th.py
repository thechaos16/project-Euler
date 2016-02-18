>>> p=''
>>> i=1
>>> while 1:
	p = p+str(i)
	if(len(p)>1000000):
		break
	i=i+1

>>> int(p[0])*int(p[9])*int(p[99])*int(p[999])*int(p[9999])*int(p[99999])*int(p[999999])