def e(n):
    if n%3==0 or n%3==2:
        return 1
    else:
        return 2*(n/3+1)


def compute(i,n):
    if i==n:
        return [1,e(i)]
    else:
        l = compute(i+1,n)
        l[0] = l[1]*e(i)+l[0]
        p = [l[1],l[0]]
        return p

def radix(n):
    r=1
    while 'true':
        n/=10
        if n==0:
            break
        r+=1
    return r

ans = compute(0,98)
ans[0]+=2*ans[1]

cnt=0
for i in range(radix(ans[0])):
    cnt+=ans[0]%10
    ans[0]/=10

print cnt
