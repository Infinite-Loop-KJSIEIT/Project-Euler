import time

def solve():
    m=0
    ans=0
    for i in range(len(prime)):
        s=prime[i]
        con=1
        for j in range(i+1,len(prime)):
            s+=prime[j]
            con+=1
            if s>=prime[-1]:
                break
            if s in search.keys() and con>m:
                m=con
                ans=s
    print("Answer",ans)
            
    

print("started")
st=time.time()
n=10**6+1
p=[True]*n
for i in range(2,n):
    for j in range(i*2,n,i):
        
        p[j]=False
prime=[]
search={}
print(time.time()-st,"sec part 1 prime")
for i in range(2,n):
    if p[i]:
        prime.append(i)
        search[i]=1

print(time.time()-st,"sec part 2 prime")       
solve()
print("done\n","Time:",time.time()-st)
        
