import math

def pri(n):
	check=1
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			check=0
			break
	return check

def pl(l):
	ans=1
	for i in range(len(l)):
		ans*=l[i]
	return ans

primes = []

for i in range(2,10000):
	if pri(i)==1:
		primes.append(i)

for i in range(1,len(primes)+1):
	temp = primes[0:i]
	ans = pl(temp)
	if ans>1000000:
		break
	ddd = ans
