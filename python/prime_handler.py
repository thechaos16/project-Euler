## Notes
## file format: prime \t prime \t ......
import numpy as np

class prime_handler:
	def __init__(self,number):
		self.number = number
		filePath = './primeLi.txt'
		## read prime
		self.pList = self.readExistedPrime(filePath)
		## get primes less than number
		[self.returnList,updateChecker] = self.primeLessThan()
		if updateChecker==1:
			## update file
			self.updatePrimeList(filePath)

	## construct existed prime list by reading a file
	def readExistedPrime(self,filePath):
		try:
			f = open(filePath,'r')
			## read all primes
			primeStr = f.readline().strip('\n').strip('')
			f.close()
			## parsing
			primeList = primeStr.split('\t')
			if len(primeList)==1:
				return []
			primeList = [int(elm) for elm in primeList]
			return primeList
		## if there is no such file, make it
		except FileNotFoundError:
			f = open(filePath,'w')
			f.close()
			return []

	## check if given number is prime
	def isPrime(self,number):
		for pri in self.pList:
			if number%pri==0:
				return 0
		return 1

	## prime less than number
	def primeLessThan(self):
		try:
			maxPrime = max(self.pList)
		except ValueError:
			maxPrime = 2
		if self.number <= maxPrime:
			pArray = np.array(self.pList)
			returnList = pArray[pArray<=self.number]
			return [returnList,0]
		for i in range(maxPrime,self.number+1):
			if i%2==0:
				continue
			if self.isPrime(i):
				self.pList.append(i)
		return [self.pList,1]
		


	## update prime list (now it's re-writing, and it should be just update for reducing time complexity)
	def updatePrimeList(self,filePath):
		## sort pList
		self.pList.sort()
		strList = [str(elm) for elm in self.pList]
		primeStr = '\t'.join(strList)
		f = open(filePath,'w')
		f.write(primeStr)
		f.close()
		

if __name__=='__main__':
	phi = prime_handler(1500)
