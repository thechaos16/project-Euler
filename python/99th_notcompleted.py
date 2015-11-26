import math

def digit(n):
    return len(str(n))

def basedigit(a,b):
    return digit(a)*b

def compare(a,b):
    bd = [basedigit(a[0],a[1]),basedigit(b[0],b[1])]
    if bd[0]>bd[1]:
        return 0
    elif bd[0]<bd[1]:
        return 1
    else:
        return 1

nominee = []
f = file('base_exp.txt','r')
for line in f:
    line = line.strip('\n')
    k = line.split(',')
    k[0] = int(k[0])
    k[1] = int(k[1])
    nominee.append(k)

maxline = 0

for i in range(1,len(nominee)):
    if compare(nominee(maxline),nominee(i))==1:
        maxline = i
