import math
n = 600851475143
i=2
while n>1:
    while n%i==0:
        n//=i
        print(n,i)
    i+=1
