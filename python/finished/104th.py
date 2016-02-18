import math

# memory for fibonacci sequence
fseq = [1,1]

# last nine digit of Fibonacci sequence
lnd = [1,1]

# first nine digit of Fibonacci sequence
fnd = [[1,0],[1,0]]


# pandigital number
def pandigit(n):
    if len(str(n))!=9:
        return 0
    temp = []
    for i in range(9):
        temp.append(n%10)
        n/=10
    for i in range(1,10):
        if i not in temp:
            return 0
    return 1
    
# fibonacci sequence
def fibo(n):
    if len(fseq)>=n:
        return fseq[n-1]
    temp = fibo(n-1)+fibo(n-2)
    fseq.append(temp)
    return temp

# last nine digit
def lfibo(n):
    if len(lnd)>=n:
        return lnd[n-1]
    temp = lfibo(n-1)+lfibo(n-2)
    if len(str(temp))>9:
        kk = str(temp)[len(str(temp))-9:]
    else:
        kk = temp
    lnd.append(int(kk))
    return int(kk)

# first nine digit
def ffibo(n):
    if len(fnd)>=n:
        return fnd[n-1][0]
    check = 0
    temp1 = ffibo(n-1)
    temp2 = ffibo(n-2)
    if fnd[n-2][1]==0:
        temp = temp1+temp2
    else:
        temp = temp1*10+temp2
    if len(str(temp))>15:
        if fnd[n-2][1]==0:
            check=1
        kk = str(temp)[:15]
    else:
        kk = temp
    fnd.append([int(kk),check])
    return int(kk)

i = 1
ldigit = []
while(1):
    temp = ffibo(i)
    temp2 = lfibo(i)
    if pandigit(temp2)==1:
        if pandigit(int(str(temp)[:9]))==1:
            ldigit.append(i)
    if i>1000000:
        break
    i+=1
