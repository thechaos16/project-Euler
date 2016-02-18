def ten(n):
    ans=1
    for i in range(n):
        ans*=2
        ans=ans%pow(10,10)
    return ans

#p = (28433*ten(7830457)+1)%pow(10,10)
