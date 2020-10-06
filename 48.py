import time

print("started")
st=time.time()
'''n=10**6
p=[True]*n
for i in range(2,n):
    for j in range(i*2,n,i):
        
        p[j]=False
prime={}
print(time.time()-st,"sec part 1 prime")
for i in range(2,n):
    if p[i]:

        prime[i]=1

print(time.time()-st,"sec part 2 prime")       
All=[0]*n
for i in prime.keys():
    for j in range(i*2,n,i):
        All[j]+=1

print(time.time()-st,"sec factors done")

for i in range(n-3):
    if All[i]==All[i+1]==All[i+2]==All[i+3]==4:
        print("Answer:",i)
        break'''
mod=10**10
print(sum(pow(i,i,mod) for i in range(1,1001))%mod)
print("done\n","Time:",time.time()-st)
        

