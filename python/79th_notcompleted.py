# candidate generator
def gen(n,res):
        if n==1:
                res2 = []
                for i in range(1,10):
                        res2.append(str(i))
                return res2
        res2 = []
        for i in range(len(res)):
                for j in range(10):
                        res2.append(res[i]+str(j))
        return res2
                        
# pw checker (n, pw -> string)
def checker(n,pw):
        pwc = 0
        res = 0
        for i in range(len(n)):
                if pw[pwc]==n[i]:
                        pwc+=1
                        res+=1
                if res==3:
                        return 1
        if res==3:
                return 1
        return 0

f = open('keylog.txt','r')
keys = []

for line in f:
        line.strip('\n')
        keys.append(line)

# checker
#keys = ['132','124','125','234','245','345']

# length of pw
lop = 1
finres = ''
cand = []
cand2 = []

# matching score
mc = 20

while(True):
        cand = gen(lop,cand2)
        cand2 = []
        if lop<3:
                lop+=1
                continue
        fin = 0
        # if all pw are not matched with candidate, discard it
        candchecker = 50
        for i in range(len(cand)):
                tempch = 0
                for j in range(len(keys)):
                        if checker(str(cand[i]),keys[j])==0:
                                candchecker-=1
                                tempch = 1
                if tempch==0:
                        fin = 1
                        finres = cand[i]
                        break
                if candchecker>=mc:
                        cand2.append(cand[i])
        if fin==1:
                print finres
                break
        lop+=1
