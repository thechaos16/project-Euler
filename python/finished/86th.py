import numpy as np
    
def is_integer_pyth(n):
    temp = np.sqrt(n)
    if int(temp)==temp:
        return 1
    return 0

def find_path(n,prev_list = None):
    if n==1:
        return []
    if prev_list==None:
        prev_list = find_path(n-1)
    for i in range(n):
        for j in range(i,n):
            if is_integer_pyth((n**2+(i+1+j+1)**2)):
                cand = [n,i+1,j+1]
                cand.sort()
                if cand not in prev_list:
                    prev_list.append(cand)
    return prev_list
    
i = 616
target = 10**6
#res = find_path(i,res)
res = find_path(i)
while True:
    i+=1
    res = find_path(i,res)
    if len(res)>=target:
        break