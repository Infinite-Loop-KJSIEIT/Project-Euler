
from fractions import Fraction  as frac
import fractions

    

num,denom=1,1
for n in range(10,100):
    for d in range(n+1,100):
        n0=n//10
        n1=n%10
        d0=d//10
        d1=d%10
        if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
            num*=n
            denom*=d
            

       
ans=frac(num,denom)
print(ans.denominator)
        


        



