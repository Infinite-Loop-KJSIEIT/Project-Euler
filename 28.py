import itertools

ans=0
for i in range(3,1002,2):
    ans+=4*i*i-6*(i-1)
print(ans+1)

