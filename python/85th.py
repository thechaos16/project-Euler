rank = []

for i in range(1,8000):
        for j in range(1,8000):
                temp = i*j*(i+1)*(j+1)
                if abs(temp-8000000)<200:
                        rank.append([i,j,temp])
                if temp>8000000:
                        break
