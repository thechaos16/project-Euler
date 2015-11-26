pri = [2,3,5]

def prime(n):
        if n in pri:
                return 1
        else:
                for i in range(len(pri)):
                        if n%pri[i]==0:
                                return 0
                pri.append(n)
                return 1


def buildpri(n):
        for i in range(5,n):
                k = prime(i)


buildpri(7072)

ans = []

for i in range(len(pri)):
        for j in range(len(pri)):
                for k in range(len(pri)):
                        temp = pow(pri[i],2)+pow(pri[j],3)+pow(pri[k],4)
                        if temp not in ans:
                                if temp<50000000:
                                        ans.append(temp)
