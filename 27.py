import itertools

a=[0]*(10**6)
for i in range(2,len(a)):
    for j in range(2*i,10**6,i):
        a[j]=1
prime=set()
for i in range(2,10**6):
    if a[i]==0:
        prime.add(i)
def isp(n):
    if n in prime:
        return True
    return False

def conp(ab):
    a,b=ab
    for i in itertools.count():
        n=i*i+i*a+b
        if not isp(n):
            return i

ans=max(((a,b) for a in range(-999,1000) for b in range(2,1000)), key=conp)
print(ans[0]*ans[1])
