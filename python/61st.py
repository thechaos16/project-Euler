>>> tri=[]
>>> sqr=[]
>>> pent=[]
>>> hexa=[]
>>> hept=[]
>>> octa=[]
>>> i=2

>>> while 1:
	if i*(i+1)/2<10000 and i*(i+1)/2>1000:
		tri.append(i*(i+1)/2)
	if i*(i+1)/2>10000:
		break
	if i*i<10000 and i*i>1000:
		sqr.append(i*i)
	if i*(3*i-1)/2<10000 and i*(3*i-1)/2>1000:
		pent.append(i*(3*i-1)/2)
	if i*(2*i-1)<10000 and i*(2*i-1)>1000:
		hexa.append(i*(2*i-1))
	if i*(5*i-3)/2<10000 and i*(5*i-3)/2>1000:
		hept.append(i*(5*i-3)/2)
	if i*(3*i-2)<10000 and i*(3*i-2)>1000:
		octa.append(i*(3*i-2))
	i=i+1


>>> store = {3:tri, 4:sqr, 5:pent, 6:hexa, 7:hept, 8:octa}

>>> def cyclic(n,x):
	l=[]
	for j in range(3,9):
		if j in x:
			continue
		k = store[j]
		pp = (n%100)*100
		for i in range(100):
			if pp+i in k:
				l.append((pp+i,j))
	return l

>>> for i in range(len(tri)):
	p1=cyclic(tri[i],[3])
	for j1 in range(len(p1)):
		exc1 = [3]
		exc1.append(p1[j1][1])
		p2 = cyclic(p1[j1][0],exc1)
		if len(p2)==0:
			exc1.remove(p1[j1][1])
			continue
		for j2 in range(len(p2)):
			exc2 = exc1
			exc2.append(p2[j2][1])
			p3 = cyclic(p2[j2][0],exc2)
			if len(p3)==0:
				exc2.remove(p2[j2][1])
				continue
			for j3 in range(len(p3)):
				exc3 = exc2
				exc3.append(p3[j3][1])
				p4 = cyclic(p3[j3][0],exc3)
				if len(p4)==0:
					exc3.remove(p3[j3][1])
					continue
				for j4 in range(len(p4)):
					exc4 = exc3
					exc4.append(p4[j4][1])
					p5 = cyclic(p4[j4][0],exc4)
					if len(p5)==0:
						exc4.remove(p4[j4][1])
						continue
					if p5[0][0]%100==tri[i]/100:
						print tri[i], p1[j1][0], p2[j2][0], p3[j3][0], p4[j4][0], p5[0][0]
						print tri[i]+p1[j1][0]+p2[j2][0]+p3[j3][0]+p4[j4][0]+p5[0][0]
						break
					exc4.remove(p4[j4][1])
				exc3.remove(p3[j3][1])
			exc2.remove(p2[j2][1])
		exc1.remove(p1[j1][1])