n=10**6+1
p=[True]*n
for i in range(2,n):
    for j in range(i*2,n,i):
        p[j]=False
print=set()
for i in range(2,n):
    if p[i]:
        prime.add(i)

for i in prime:
    
