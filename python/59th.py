def binary(n):
	l=[]
	x=n
	while 1:
		l.insert(0,n%2)
		n=n/2
		if n==0:
			break
	return l

def deci(n):
	ans=0
	for i in range(len(n)):
		ans = ans+n[i]*pow(2,len(n)-i-1)
	return ans

def xor(a,b):
	la = binary(a)
	lb = binary(b)
	lena = len(la)
	lenb = len(lb)
	ans=[]
	if lena>lenb:
		for i in range(lena-lenb):
			lb.insert(0,0)
	elif lenb>lena:
		for i in range(lenb-lena):
			la.insert(0,0)
	for i in range(len(la)):
		if la[i]==lb[i]:
			p=0
		else:
			p=1
		ans.append(p)
	result = deci(ans)
	return result

fp = open('cipher1.txt','r')
for line in fp:
	read = line
read.strip('\n')
cipher = read.split(',')

for i in range(97,123):
	for j in range(97,123):
		for k in range(97,123):
			result=''
			for m in range(len(cipher)):
				if m%3==0:
					result = result+chr(xor(int(cipher[m]),i))
				elif m%3==1:
					result = result+chr(xor(int(cipher[m]),j))
				else:
					result = result+chr(xor(int(cipher[m]),k))
			check=1
			for m in range(len(result)):
				if ord(result[m])>122 or ord(result[m])<40:
					check=0
					break
			if check==1:
				print result