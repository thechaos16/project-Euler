>>> fp = file('triangle.txt','r')
>>> l=[]
>>> for line in fp:
	l.append(line)

>>> p=[]
>>> for i in range(len(l)):
	l[i] = l[i].strip()
	p.append(l[i].split(' '))

>>> def sp(i,j):
	if (i,j) in dynamic:
		return dynamic[i,j]
	if i==j:
		ans = sp(i-1,j-1)+int(p[i][j])
		dynamic[i,j] = ans
		return ans
	elif j==0:
		ans = sp(i-1,j)+int(p[i][j])
		dynamic[i,j] = ans
		return ans
	else:
		ans = max(sp(i-1,j),sp(i-1,j-1))+int(p[i][j])
		dynamic[i,j] = ans
		return ans

>>> sol = 0
>>> for i in range(100):
	sss = sp(99,i)
	sol = max(sss,sol)