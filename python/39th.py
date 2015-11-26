def istri(a,b,c):
	if c<a+b:
		return 1
	return 0

def isright(a,b,c):
	if pow(c,2)==pow(a,2)+pow(b,2):
		return 1
	return 0

ans=0

cnt=0

for i in range(10,1001):
	val=[]
	for a in range(1,i/3+1):
		for b in range(a,i/2):
			c = i-a-b
			if istri(a,b,c)==0:
				continue
			if isright(a,b,c)==1:
				val.append([a,b,c])
	if len(val)>cnt:
		cnt=len(val)
		ans=i