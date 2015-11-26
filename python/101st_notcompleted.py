def poly(n):
    return 1-n+pow(n,2)-pow(n,3)+pow(n,4)-pow(n,5)+pow(n,6)-pow(n,7)+pow(n,8)-pow(n,9)+pow(n,10)

def poly2(data,n):
    ans=0
    for i in range(len(data)):
        ans = data[i]*pow(n,i)
    return ans

def cand(dim,data):
    l = []
    for i in range(dim+1):
        l.append(0)
    for i in range(dim+1):
        poly2(l,i)
    return l

seq = []
for i in range(1,100):
    seq.append(poly(i))

i=1
ans=0
while 1:
    dim = i-1
    cand(dim,seq[0:i-1])
    bop = 
    if(i==11):
        break
    i+=1
