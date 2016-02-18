>>> fp = file("names.txt","r")
>>> read=[]
>>> for line in fp:
	read.append(line)

>>> store = read[0].split(",")

>>> for i in range(len(store)):
	store[i] = store[i].strip('"')

>>> store.sort()

>>> dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

>>> ans=0

>>> for i in range(len(store)):
	cnt=0
	for j in range(len(store[i])):
		cnt=cnt+dic[store[i][j]]
	ans = ans+cnt*(i+1)