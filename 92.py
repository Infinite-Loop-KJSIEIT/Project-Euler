import time
def res(x):
    ans=0
    while x>0:
        r=x%10
        ans+=r*r
        x//=10
    return ans
def ter(x,vis):
    a=[]
    a.append(x)
    while vis[x]==0:
        x=res(x)
        a.append(x)
    for i in a:
        vis[i]=vis[x]
    
    


st=time.time()
lim=10**7
vis=[0]*lim
vis[1]=1
vis[89]=89

for i in range(1,lim):
    if not vis[i]:
        ter(i,vis)
print(sum(1 for i in vis if i==89))
print(time.time()-st,'s')
        

