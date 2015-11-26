>>> fp = file('poker.txt','r')

>>> l=[]
>>> for line in fp:
	l.append(line)

>>> order = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

>>> def highest(l):
	high = 1
	for i in range(len(l)):
		if order[l[i][0]]>high:
			ans = l[i][0]
			high = order[l[i][0]]
	return ans

>>> def isOnepair(l):
	for i in range(len(l)):
		for j in range(len(l)):
			if i!=j and l[i][0]==l[j][0]:
				return l[i][0]
	return '0'

>>> def isTwopair(l):
	cnt=0
	num = []
	for i in range(len(l)):
		for j in range(len(l)):
			if i!=j and l[i][0]==l[j][0]:
				if l[i][0] in num:
					continue
				num.append(l[i][0])
				cnt = cnt+1
	if cnt==2:
		num.sort()
		return num
	else:
		return '0'

>>> def isTriple(l):
	for i in range(len(l)):
			for j in range(len(l)):
				for k in range(len(l)):
					if i!=j and j!=k and k!=i and l[i][0]==l[j][0]==l[k][0]:
						return l[i][0]
	return '0'

>>> def isStraight(l):
	num = []
	for i in range(len(l)):
		num.append(order[l[i][0]])
	num.sort()
	if(num[0]==2 and num[1]==3 and num[2]==4 and num[3]==5 and num[4]==14):
		return num
	for i in range(len(l)-1):
		if num[i]+1!=num[i+1]:
			return '0'
	return num

>>> def isFlush(l):
	check = l[0][1]
	for i in range(1,len(l)):
		if l[i][1]!=check:
			return '0'
	return check

>>> def isFullhouse(l):
	ans = []
	ans.append(isTriple(l))
	if ans[0]=='0':
		return '0'
	for i in range(len(l)):
		for j in range(len(l)):
			if i!=j and l[i][0]!=ans[0] and l[i][0]==l[j][0]:
				ans.append(l[i][0])
				return ans
	return '0'

>>> def isFourcard(l):
	cnt1=1
	cnt2=1
	check1 = l[0][0]
	check2 = l[1][0]
	if(check1==check2):
		cnt1=2
	for i in range(2,len(l)):
		if l[i][0]==check1:
			cnt1 = cnt1+1
		elif l[i][0]==check2:
			cnt2 = cnt2+1
	if cnt1==4:
		return check1
	if cnt2==4:
		return check2
	return '0'

>>> def isSF(l):
	a = isFlush(l)
	b = isStraight(l)
	if a=='0' or b=='0':
		return '0'
	l=[]
	l.append(a)
	l.append(b)
	return l

>>> def isRF(l):
	a = isSF(l)
	if a=='0':
		return '0'
	if a[1] == [10,11,12,13,14]:
		return a[0]
	return '0'

>>> def winner(l1, l2):
	result1 = 0
	result2 = 0
	highest1 = order[highest(l1)]
	highest2 = order[highest(l2)]
	if isOnepair(l1)!='0':
		result1 = 1
	if isTwopair(l1)!='0':
		result1 = 2
	if isTriple(l1)!='0':
		result1 = 3
	if isStraight(l1)!='0':
		result1 = 4
	if isFlush(l1)!='0':
		result1 = 5
	if isFullhouse(l1)!='0':
		result1 = 6
	if isFourcard(l1)!='0':
		result1 = 7
	if isSF(l1)!='0':
		result1 = 8
	if isRF(l1)!='0':
		result1 = 9
	if isOnepair(l2)!='0':
		result2 = 1
	if isTwopair(l2)!='0':
		result2 = 2
	if isTriple(l2)!='0':
		result2 = 3
	if isStraight(l2)!='0':
		result2 = 4
	if isFlush(l2)!='0':
		result2 = 5
	if isFullhouse(l2)!='0':
		result2 = 6
	if isFourcard(l2)!='0':
		result2 = 7
	if isSF(l2)!='0':
		result2 = 8
	if isRF(l2)!='0':
		result2 = 9
	if result1>result2:
		return 1
	elif result1<result2:
		return 2
	else:
		if result1==1:
			x1 = order[isOnepair(l1)]
			x2 = order[isOnepair(l2)]
			if x1>x2:
				return 1
			elif x1<x2:
				return 2
		elif result1==2:
			x1 = order[isTwopair(l1)]
			x2 = order[isTwopair(l2)]
			if x1[1]>x2[1]:
				return 1
			elif x1[1]<x2[1]:
				return 2
			else:
				if x1[0]>x2[0]:
					return 1
				elif x1[0]<x2[0]:
					return 2
		elif result1==3:
			x1 = order[isTriple(l1)]
			x2 = order[isTriple(l2)]
			if x1>x2:
				return 1
			elif x1<x2:
				return 2
		elif result1==6:
			x1 = order[isFullhouse(l1)]
			x2 = order[isFullhouse(l2)]
			if x1[0]>x2[0]:
				return 1
			elif x1[0]<x2[0]:
				return 2
			else:
				if x1[1]>x2[1]:
					return 1
				elif x1[1]<x2[1]:
					return 2
		elif result1==7:
			x1 = order[isFourcard(l1)]
			x2 = order[isFourcard(l2)]
			if x1>x2:
				return 1
			elif x1<x2:
				return 2
		if highest1>highest2:
			return 1
		elif highest1<highest2:
			return 2
		else:
			return 0

>>> win1=0
>>> win2=0

>>> for i in range(len(l)):
	p = l[i].split(' ')
	p1=[]
	p2=[]
	for j in range(len(p)):
		if(j<5):
			p1.append(p[i])
		else:
			p2.append(p[i])
	if winner(p1,p2)==1:
		win1=win1+1
	elif winner(p1,p2)==2:
		win2=win2+1