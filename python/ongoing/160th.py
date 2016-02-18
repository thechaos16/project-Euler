
def last_six_digit_parser(number):
    remove_zero = str(number).rstrip('0')
    if len(remove_zero)<=6:
        return int(remove_zero)
    return int(remove_zero[-6:])
    
def factorial(n):
    if n==1 or n==0:
        return 1
    init = 1        
    for i in range(2,n+1):
        init*=i
        if init<10e5:
            continue
        if i%5==0:
            init = last_six_digit_parser(int(init))
        else:
            init = init%10e5
    return init

def run():
    number = 1000000000000
    #number = 100000000
    kk = factorial(number)
    return kk