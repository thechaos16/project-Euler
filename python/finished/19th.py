>>> Jan=31
>>> Feb=28
>>> Feb4=29
>>> Mar=31
>>> Apr=30
>>> May=31
>>> Jun=31
>>> Jun=30
>>> Jul=31
>>> Aug=31
>>> Sep=30
>>> Oct=31
>>> Nov=30
>>> Dec=31
>>> year=1901
>>> bom = 2
>>> p = (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)
>>> p1 = (Jan,Feb4,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)
>>> cnt=0
for year in range(1901,2001):
	for i in range(12):
		if year%4==0:
			bom=bom+p1[i]%7
			bom=bom%7
		else:
			bom=bom+p[i]%7
			bom=bom%7
		if bom==0:
			cnt=cnt+1