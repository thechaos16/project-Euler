def ans(num):
    if num==2:
        return [[1,1]]
    else:
        temp = ans(num-1)
        res = []
        for i in range(len(temp)):
            temp2 = [1]+temp[i]
            if temp2 not in res:
                res.append([1]+temp[i])
            for j in range(len(temp[i])):
                temp2 = []
                if j!=0:
                    if temp[i][j]==temp[i][j-1]:
                        continue
                for k in range(len(temp[i])):
                    if k==j:
                        temp2.append(temp[i][k]+1)
                    else:
                        temp2.append(temp[i][k])
                temp2.sort()
                if temp2 not in res:
                    res.append(temp2)
        return res
