fr = [[1,2]]

def radix(n):
    i=1
    while 'true':
        n/=10
        if n==0:
            break
        i+=1
    return i

def fraction(n):
    if n<=len(fr):
        return fr[n-1]
    #if n==1:
    #    return [1,2]
    l = fraction(n-1)
    fr.append([l[1],2*l[1]+l[0]])
    return [l[1],2*l[1]+l[0]]

def appsqrt(n):
    l = fraction(n)
    return [l[0]+l[1],l[1]]

cnt=0

for i in range(1,1001):
    l = appsqrt(i)
    if radix(l[0])>radix(l[1]):
        cnt+=1

print cnt
