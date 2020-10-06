import time

def dig(x, y):
	return sorted(str(x)) == sorted(str(y))

def solve():
    count=0
    for n in range(1,101):
        for r in range(1,n):
            ans=f[n]/(f[r]*f[n-r])
            if ans>10**6:
                count+=1
    print(count)
            
    

print("started")
st=time.time()
'''
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

print(time.time()-st,"sec part 2 prime")       '''
f=[1]*101
for i in range(2,101):
    f[i]=f[i-1]*i
solve()
print("done\n","Time:",time.time()-st)
        

