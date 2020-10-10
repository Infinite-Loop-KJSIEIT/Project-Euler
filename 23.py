n=28124
div=[0]*n
for i in range(1,n):
    for j in range(i*2,n,i):
        div[j]+=i
ab=[]
for i in range(n):
    if div[i]>i:
        ab.append(i)

l=[False]*n
for i in ab:
    for j in ab:
        if i+j<n:
            l[i+j]=True
ans=0
for i in range(n):
    if not l[i]:
        ans+=i
print(ans)

