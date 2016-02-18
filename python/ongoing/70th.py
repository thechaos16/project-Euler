import time
import numpy as np

def perm(a,b):
    a = str(a)
    b = str(b)
    if len(a)!=len(b):
        return 0
    if sorted(a)==sorted(b):
        return 1
    return 0

## need to be improved
def relapri(a,b):
	x,y = max(a,b), min(a,b)
	if x%y==0:
		return 0
	for i in range(2,int(np.ceil(np.sqrt(y)))):
		if y%i==0:
			if x%i==0 or x%(y/i)==0:
				return 0
	return 1

def euler(n):
    cnt=1
    notLi = []
    for i in range(2,n):
        check = 0
        for j in notLi:
            if i%j==0:
                check=1
                break
        if check:
            continue
        if relapri(i,n)==1:
            cnt+=1
        else:
            notLi.append(i)
    return cnt

def run():
    minimum = 1.2
    ans = 0
    start = time.clock()
    for i in range(10001,100000):
        temp = euler(i)
        if perm(i,temp):
            if float(i)/float(temp)<minimum:
                minimum = float(i)/float(temp)
                ans = i
    end = time.clock()
    print("%.2gs" % (end-start))
    return ans
