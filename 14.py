import math, itertools

num=m=0
for i in range(2,10**6):       
            
    x=i
    ch=1
    while x!=1:
        if x%2==0:
            x//=2
        else:
            x=x*3+1
        ch+=1
    if ch>m:
        m=ch
        num=i
print(num,ch)
        

