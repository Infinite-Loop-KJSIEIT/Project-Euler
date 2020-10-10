import math
def lcm(a,b): 
    return (a*b) // math.gcd(a,b)
ans=1
for i in range(1,21):
    ans=lcm(ans,i)
print(ans)
