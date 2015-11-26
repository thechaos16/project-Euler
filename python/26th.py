def recur(n):
    ans = [[1,n]]
    a=1
    while 1:
        a = (a%n)*10
        if [a,n] in ans or a==0:
            ans.append([a,n])
            break
        ans.append([a,n])
        
    return ans


maximum = 0
ans=0
for i in range(2,1000):
    temp = recur(i)
    if len(temp)>maximum:
        maximum = len(temp)
        ans = i
