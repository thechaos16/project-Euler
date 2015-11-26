def divisor(a):
	cnt = 0
	for i in range(1,a+1):
		if a%i==0:
			cnt=cnt+1
	return cnt

for i in range(20000):
	sum = i*(i+1)/2
	if i%2==0:
		if divisor(i/2)*divisor(i+1)>500:
			break
	else:
		if divisor(i)*divisor((i+1)/2)>500:
			break
	sum=0