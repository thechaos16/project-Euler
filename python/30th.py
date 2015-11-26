for i in range(2,1000000):
	add=0
	for j in range(len(str(i))):
		add=add+fif(int(str(i)[j]))
	if i==add:
		ans=ans+i