for i in range(20):
	for j in range(20):
		if (i+3)<20:
			value = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
			if value>m:
				m=value
			if (j+3)<20:
				value = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
				if value>m:
					m=value
		if (j+3)<20:
			value = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
			if value>m:
				m=value
			if (i-3)>=0:
				value = a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3]
				if value>m:
					m=value
	print m