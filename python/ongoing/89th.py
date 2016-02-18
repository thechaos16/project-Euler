# Roman dictionary
rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


# convert Roman to Arabian
def rta(st):
    temp = st[0]
    tempres = st[0]
    res = []
    for i in range(1, len(st)):
        if st[i] == temp:
            tempres += st[i]
        else:
            res.append(tempres)
            temp = st[i]
            tempres = st[i]
    res.append(tempres)

    ans = 0
    check = 1000
    for i in range(len(res)):
        ans += rome[res[i][0]] * len(res[i])
        if order.index(res[i][0]) > check:
            ans -= rome[order[check]] * 2
        check = order.index(res[i][0])

    return ans

# best Roman number


def brome(num):
    res = ''
    temp = str(num)
    for i in range(len(temp))[::-1]:
        if int(temp[i]) == 9:
            res = '' + res

def run(required_file):
    fp = open(required_file, 'r')
    l = []
    
    for line in fp:
        pp = line.strip('\n')
        l.append(pp)
    return l
