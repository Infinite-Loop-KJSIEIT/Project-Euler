
div=[0]*10000

for i in range(1,10000):
    for j in range(i*2,10000,i):
        div[j]+=i
ans=0
for i in range(1,10000):
    j=div[i]
    if j!=i and j<10000 and div[j]==i:
        ans+=i
print(ans)
        
print(div[:100])
