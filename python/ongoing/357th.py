import math
import sys
try:
    import modules.prime_handler as ph
except ImportError:
    sys.path.append('../')
    import modules.prime_handler as ph

def divisors(n):
    div = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i not in div:
                div.append(i+n/i)
    return div

def checker(n,obj = None):
    div = divisors(n)
    dd=0
    for i in range(len(div)):
        if obj.is_prime(div[i])==0:
            dd=1
            break
    if dd==0:
        return 1
    return 0

def run():    
    phi = ph.PrimeHandler(100000000)
    #phi = ph.PrimeHandler(10000000)
    prime_list = phi.get_prime_list()
    print('list is finished')
    cnt=0
    for prime in prime_list:
        if checker(prime-1,phi):
            #print(prime-1)
            cnt+=prime-1
    return cnt

if __name__=='__main__':
    pass