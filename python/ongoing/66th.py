import sys
import numpy as np
try:
    import modules.prime_handler as ph
except ImportError:
    sys.path.append('../')
    import modules.prime_handler as ph

def run(input_int=1000):
    phi = ph.PrimeHandler(input_int)
    prime_list = phi.get_prime_list()
    input_list = range(input_int)
    [x,res] = get_result(prime_list)
    #[x,res] = get_result(input_list)
    return [x,res]


def is_perfect_square(n):
    sqrt_res = np.sqrt(n)
    if sqrt_res==int(sqrt_res):
        return True
    return False


def equation_solver(d):
    if is_perfect_square(d)==1:
        return -1
    temp_x = 2
    while(True):
        intermediate_res = (temp_x+1)*(temp_x-1)
        ## intermediate_res should be in the form of d^(2i+1)*alpha^2
        if intermediate_res%d==0:
            intermediate_res/=d
            if is_perfect_square(intermediate_res):
                return [temp_x,np.sqrt(intermediate_res)]
        temp_x+=1

def get_result(input_list):
    x = -1
    for i in input_list:
        if is_perfect_square(i)==1:
            continue
        [tempx, tempy] = equation_solver(i)
        if x<=tempx:
            x = tempx
            res = i
            print([x, res, tempy])
    return [x, res]
    
if __name__=='__main__':
    [a,b] = run(1000)