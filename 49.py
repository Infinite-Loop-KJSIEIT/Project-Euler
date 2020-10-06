import time


def dig(x, y):
	return sorted(str(x)) == sorted(str(y))

def solve():
    for i in prime.keys():
        for step in range(1,10**4):
            b=i+step
            c=b+step
            if b in prime.keys() and c in prime.keys() and dig(i,b) and dig(b,c):
                if i!=1487:
                    print(str(i)+str(b)+str(c))
                    return

print("started")
st=time.time()
n=10**5
p=[True]*n
for i in range(2,n):
    for j in range(i*2,n,i):
        
        p[j]=False
prime={}
print(time.time()-st,"sec part 1 prime")
for i in range(2,n):
    if p[i] and len(str(i))==4:
        prime[i]=1
solve()

            

print(time.time()-st,"sec part 2 prime")       

print("done\n","Time:",time.time()-st)
        
