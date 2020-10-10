import math
m=0
for i in range(100,1000):
    for j in range(100,1000):
        ans=str(i*j)
        if ans==ans[::-1] and int(ans)>m:
            m=int(ans)
print(m)
            
        
