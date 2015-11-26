def deci(n):
    if n%10==0:
        return 1
    return 0

def percent(n):
    return n%100

temp = 1
end = 1000000000001
pp = 10000
asdf = 2

while 1:
    for i in range(asdf,pp):
        while 1:
            if deci(i)==0:
                break
            else:
                i/=10
        i = percent(i)
        temp = temp*i
        while 1:
            if deci(temp)==0:
                break
            else:
                temp = temp/10
        temp = temp%100000
    if pp==end:
        break
    asdf = pp+1
    pp*=10
    print pp
    if pp==end-1:
        pp+=1
