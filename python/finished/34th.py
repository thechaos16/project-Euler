store={0:1,1:1}

def fact(n):
	if n in store:
		return store[n]
	p = n*fact(n-1)
	store[n]=p
	return p

def check(n):
	ans=0
	k=n
	for i in range(len(str(n))):
		ans=ans+fact(k%10)
		k=k/10
	if n==ans:
		return 1
	return 0

cnt=[]

for i in range(3,9999999):
	if check(i)==1:
		cnt.append(i)