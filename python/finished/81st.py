fp = file('matrix.txt','r')
l=[]

memo = []

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
        for j in range(80):
                memo[i].append(0)

def optipath(i,j):
        if memo[i][j]!=0:
                return memo[i][j]
        x = int(p[i][j])
        if i==0:
                if j==0:
                        memo[i][j] = x
                else:
                        temp = optipath(i,j-1)
                        memo[i][j] = x+temp
        else:
                if j==0:
                        memo[i][j] = x+optipath(i-1,j)
                else:
                        p1 = optipath(i-1,j)
                        p2 = optipath(i,j-1)
                        if p1>p2:
                                memo[i][j] = x+p2
                        else:
                                memo[i][j] = x+p1
        return memo[i][j]


#add memoization
