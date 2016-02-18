goal = 10000000

memo = []

# next number for chain
def chain(n):
        string = str(n)
        ans = 0
        for i in range(len(string)):
                temp = int(string[i])
                temp2 = temp*temp
                ans+=temp2
        return ans

# end of chain
def eoc(n):
        p = n
        ch = [p]
        while 1:
             p = chain(p)
             ch.append(p)
             if p==1 or p==89:
                     for i in range(len(ch)):
                             memo[ch[i]-1] = p
                     return p

temp = 0

for i in range(goal):
        memo.append(0)

for i in range(1,goal+1):
        if memo[i-1]==0:
                temp = eoc(i)

print memo.count(89)
