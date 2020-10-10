import math, itertools

def fac(n):
    f=1
    for i in range(1,n+1):
       f*=i
    return f
print(fac(40)/fac(20)**2)

