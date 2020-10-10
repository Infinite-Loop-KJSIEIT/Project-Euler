import itertools

def rc(n):
    x=1
    seen={}
    for i in itertools.count():
        if x in seen:
            return i-seen[x]
        else:
            seen[x]=i
            x*=10
            x%=n
            

print(max(range(1,1000),key=rc))


    
