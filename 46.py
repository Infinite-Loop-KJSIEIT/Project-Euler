def check(num):
    for j in range(1,num//2+1):
        if num-2*j*j in prime.keys():
            return True
    return False


n=10**6
p=[True]*n
for i in range(2,n):
    for j in range(i*2,n,i):
        
        p[j]=False
prime={}

for i in range(2,n):
    if p[i]:

        prime[i]=1

        



print("prime taken")
for i in range(9,10**6,2):
    if i in prime.keys():
        continue
    if not check(i):
        print(i)
        break
        
