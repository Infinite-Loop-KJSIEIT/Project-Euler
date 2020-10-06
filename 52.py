import time

def dig(x, y):
	return sorted(str(x)) == sorted(str(y))

def solve():
    n=10**6+1
    for i in range(1,n):
        a=i
        b=i*2
        c=i*3
        d=i*4
        e=i*5
        f=i*6
        if dig(a,b) and dig(b,c) and dig(c,d) and dig(d,e) and dig(e,f):
            print("Answer:",i)
            return
            
    

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
solve()
print("done\n","Time:",time.time()-st)
        

