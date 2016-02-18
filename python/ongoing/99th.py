def digit(n):
    return len(str(n))

def basedigit(a,b):
    return (digit(a)-1)*b+1

def compare(a,b):
    bd = [basedigit(a[0],a[1]),basedigit(b[0],b[1])]
    if bd[0]>bd[1]:
        return 0
    elif bd[0]<bd[1]:
        return 1
    else:
        print(str(bd[0])+'\t'+str(bd[1]))
        return 1

def run(required_file):
    nominee = []
    f = open(required_file,'r')
    for line in f:
        line = line.strip('\n')
        k = line.split(',')
        k[0] = int(k[0])
        k[1] = int(k[1])
        nominee.append(k)
    
    maxline = 0
    
    for i in range(1,len(nominee)):
        if compare(nominee[maxline],nominee[i])==1:
            maxline = i
    return maxline
