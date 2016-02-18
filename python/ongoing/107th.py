# check if there's path between A and B
def ispath(mat,a,b):
    if mat[a][b]!=-1:
        return 1
    visited = [b]
    check = 0
    while 1:
        if check==1:
            return 0
        check = 1
        for i in range(len(visited)):
            for j in range(len(mat[visited[i]])):
                if mat[visited[i]][j]!=-1:
                    if j in visited:
                        continue
                    if mat[a][j]!=-1:
                        return 1
                    visited.append(j)
                    check = 0
                    

# shortest path from A to B (Dijkstra)
def dijkstra(mat,a,b):
    # path
    path = []
    # weight
    tempmat = []
    # visited nodes
    visited = []
    for i in range(len(mat)):
        # source
        if i==a:
            tempmat.append(0)
            path.append([])
        # initial value (unvisited)
        else:
            tempmat.append(-1)
            path.append([])

    # altorithm starts
    # current node (source)
    cnode = a
    
    while 1:
        if b in visited:
            break
        for i in range(len(mat[cnode])):
            if mat[cnode][i]!='-':
                temp = tempmat[cnode]+int(mat[cnode][i])
                if tempmat[i]==-1:
                    tempmat[i] = temp
                    path[i] = path[cnode]+[i]
                else:
                    if tempmat[i]>temp:
                        tempmat[i] = temp
                        path[i] = path[cnode]+[i]
        visited.append(cnode)
        # select new current node
        tempval = 100000
        for i in range(len(tempmat)):
            if i not in visited and tempmat[i]!=-1:
                if tempmat[i]<tempval:
                    tempval = tempmat[i]
                    cnode = i
        
    return path[b]

# update new path
def update(temp,mat,newmat):
    for i in range(len(temp)-1):
        newmat[temp[i]][temp[i+1]] = int(mat[temp[i]][temp[i+1]])

# single-source shortest path for all vertices
def sssp(mat):
    # trimmed matrix
    newmat = []
    for i in range(len(mat)):
        temp = []
        for j in range(len(mat)):
            temp.append(-1)
        newmat.append(temp)

    # sssp 
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            temp = dijkstra(mat,i,j)
            # update newpath
            update(temp,mat,newmat)
            
    return newmat

# find largest edge
def large(mat):
    temp = -1
    loc = [-1,-1]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]>temp:
                temp = mat[i][j]
                loc[0] = i
                loc[1] = j
    return loc

# sorting edge by its weight
def sortedge(mat):
    res = []
    opt = []
    for i in range(len(mat)):
        temp  = []
        for j in range(len(mat[i])):
            temp.append(mat[i][j])
        opt.append(temp)
    while 1:
        loc = large(opt)
        if opt[loc[0]][loc[1]]==-1:
            return res
        res.append(loc)
        opt[loc[0]][loc[1]]=-1

# reduce
def red(mat):
    opt = []
    for i in range(len(mat)):
        temp  = []
        for j in range(len(mat[i])):
            temp.append(mat[i][j])
        opt.append(temp)

    '''while 1:
        loc = large(opt)
        temp = opt[loc[0]][loc[1]]
        opt[loc[0]][loc[1]] = -1
        if ispath(opt,loc[0],loc[1])==0:
            opt[loc[0]][loc[1]] = temp
            break'''

    res = sortedge(opt)
    for i in range(len(res)):
        temp = opt[res[i][0]][res[i][1]]
        opt[res[i][0]][res[i][1]] = -1
        if ispath(opt,res[i][0],res[i][1])==0:
            opt[res[i][0]][res[i][1]] = temp
    
    return opt

# weight of network
def won(mat):
    cnt = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
           if mat[i][j]!=-1 and mat[i][j]!='-':
               cnt+=int(mat[i][j])
    return cnt

def run(required_file):
    f = open(required_file,'r')
    mat = []
    for line in f:
        line = line.strip('\n')
        temp = line.split(',')
        mat.append(temp)
    
    # algorithms
    # delete every edge except 780 SSSPs
    # delete largest edge until it breaks condition
    # sssp
    trimmed = sssp(mat)
    # delete largest edge until terminal condition
    ans = red(trimmed)
    # answer
    res = won(ans)
    return res
