def penta(n):
	return n*(3*n-1)/2

def hexa(n):
	return n*(2*n-1)

i=144

while 1:
	check=0
	j=165
	while 1:
		if hexa(i)==penta(j):
			check=1
			print i,j,hexa(i)
			break
		elif hexa(i)<penta(j):
			break
		j=j+1
	if check==1:
		break
	i=i+1

