import math
ans=0
for i in range(1,10000):
    for j in range(1,int(math.sqrt(i))):
        if i%j==0:
            temp=str(i)+str(j)+str(i//j)
            if "".join(sorted(temp))=="123456789":
                ans+=i
                break

print(ans)
            
                
