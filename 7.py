import math
p=set()
p.add(2)
x=3
ans=2
while len(p)!=10001:
    flag=True
    for i in p:
        if x%i==0:
            flag=False
            break
    if flag:
        p.add(x)
        ans=x
    x+=2
print(ans)
    
        
        
