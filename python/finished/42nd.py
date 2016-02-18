>>> def tri(n):
	sum = 0
	i=1
	while 1:
		sum = sum+i
		if(n==sum):
			return 1
		elif(n<sum):
			return 0
		i=i+1

>>> alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '"':0}

>>> for i in range(len(word)-1):
	value = 0
	for j in range(len(word[i])-1):
		value = value+alpha[word[i][j]]
	if(tri(value)==1):
		cnt=cnt+1

		
>>> cnt