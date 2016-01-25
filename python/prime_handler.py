## Notes
## file format: prime \t prime \t ......
import numpy as np

class PrimeHandler:
    def __init__(self,number,file_path=None):
        self.number = number
        if file_path is None:
            file_path = './prime_list.txt'
        ## read prime
        self.prime_list = self.read_exsited_prime(file_path)
        ## get primes less than number
        [self.return_list,update_checker] = self.prime_less_than()
        if update_checker:
            ## update file
            self.update_prime_list(file_path)

	## construct existed prime list by reading a file
    def read_exsited_prime(self,file_path):
        try:
            f = open(file_path,'r')
            ## read all primes
            prime_string = f.readline().strip('\n').strip('')
            f.close()
            ## parsing
            prime_list = prime_string.split('\t')
            if len(prime_list):
                return []
            prime_list = [int(elm) for elm in prime_list]
            return prime_list
        ## if there is no such file, make it
        except FileNotFoundError:
            f = open(file_path,'w')
            f.close()
            return []

    ## check if given number is prime
    def is_prime(self,number):
        for pri in self.prime_list:
            if number%pri==0:
                return 0
        return 1

    ## prime less than number
    def prime_less_than(self):
        try:
            max_prime = max(self.prime_list)
        except ValueError:
            max_prime = 2
    
        if self.number <= max_prime:
            prime_array = np.array(self.pirme_list)
            return_list = prime_array[prime_array<=self.number]
            return [return_list,False]
        for i in range(max_prime,self.number+1):
            if i%2==0:
                continue
            if self.is_prime(i):
                self.prime_list.append(i)
        return [self.prime_list,True]

    ## update prime list (now it's re-writing, and it should be just update for reducing time complexity)
    def update_prime_list(self,file_path):
        ## sort pList
        self.prime_list.sort()
        string_list = [str(elm) for elm in self.prime_list]
        prime_string = '\t'.join(string_list)
        f = open(file_path,'w')
        f.write(prime_string)
        f.close()

    def get_prime_list(self):
        return self.return_list
		

if __name__=='__main__':
	phi = PrimeHandler(15000)
