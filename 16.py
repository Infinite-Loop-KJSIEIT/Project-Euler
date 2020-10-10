import math, itertools

a=str(2**1000)
ans=0
for i in a:
    ans+=ord(i)-48
print(ans)
