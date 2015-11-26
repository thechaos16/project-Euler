def optpath(data,res,out,s,t):
        ind = [s[1],s[0]]
        res[s[0]][s[1]] = 0
        while 1:
                # -1: up, 0:right, 1: down, 5: deadlock
                nextind = 5
                mincheck = -1
                if out[t[0]][t[1]]==1:
                        break
                if ind[1]<len(data[0])-1:
                        if out[ind[1]+1][ind[0]]==0:
                                if res[ind[1]+1][ind[0]]==-1:
                                        res[ind[1]+1][ind[0]] = res[ind[1]][ind[0]]+data[ind[1]][ind[0]]
                                else:
                                        res[ind[0]+1][ind[1]] = min(res[ind[0]+1][ind[1]],res[ind[0]][ind[1]]+data[ind[0]][ind[1]])
                                if mincheck>res[ind[0]+1][ind[1]] or mincheck==-1:
                                        mincheck = res[ind[0]+1][ind[1]]
                                        nextind = 0
                if ind[0]!=0:
                        if out[ind[1]][ind[0]-1]==0:
                                if res[ind[1]][ind[0]-1]==-1:
                                        res[ind[1]][ind[0]-1] = res[ind[1]][ind[0]]+data[ind[1]][ind[0]]
                                else:
                                        res[ind[1]][ind[0]-1] = min(res[ind[1]][ind[0]-1],res[ind[1]][ind[0]]+data[ind[1]][ind[0]])
                                if mincheck>res[ind[1]][ind[0]-1] or mincheck==-1:
                                        mincheck = res[ind[1]][ind[0]-1]
                                        nextind = -1     
                if ind[0]<len(data)-1:
                        if out[ind[1]][ind[0]+1]==0:
                                if res[ind[1]][ind[0]+1]==-1:
                                        res[ind[1]][ind[0]+1] = res[ind[1]][ind[0]]+data[ind[1]][ind[0]]
                                else:
                                        res[ind[1]][ind[0]+1] = min(res[ind[1]][ind[0]+1],res[ind[1]][ind[0]]+data[ind[1]][ind[0]])
                                if mincheck>res[ind[1]][ind[0]+1] or mincheck==-1:
                                        mincheck = res[ind[1]][ind[0]+1]
                                        nextind = 1
                out[ind[1]][ind[0]] = 1
                if nextind==-1:
                        ind[0] = ind[0]-1
                elif nextind==0:
                        ind[1] = ind[1]+1
                elif nextind==1:
                        ind[0] = ind[0]+1                
                else:
                        return -1
        return res[t[0]][t[1]]


fp = file('matrix.txt','r')
l=[]

memo = []
outout = []

for line in fp:
	l.append(line)
p=[]
for i in range(len(l)):
	p.append(l[i].split(','))

for i in range(len(p)):
	m = p[i][79].split('\n')
	p[i][79] = m[0]

for i in range(80):
        memo.append([])
        outout.append([])
        for j in range(80):
                p[i][j] = int(p[i][j])
                memo[i].append(-1)
                outout[i].append(0)

minmin = -1
for i in range(len(p)):
        for j in range(len(p)):                
                memo = []
                outout = []
                for ii in range(80):
                        memo.append([])
                        outout.append([])
                        for jj in range(80):
                                memo[ii].append(-1)
                                outout[ii].append(0)
                check = optpath(p,memo,outout,[i,0],[j,len(p[0])-1])
                if check==-1:
                        continue
                if minmin==-1:
                        minmin = check
                if check<minmin:
                        minmin = check
                        print [[i,0],[j,len(p[0])-1]]
