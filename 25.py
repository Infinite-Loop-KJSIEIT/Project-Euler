import itertools

a,b=0,1
for i in itertools.count():
    if len(str(a))==1000:
        print(i)
        break
    a,b=b,a+b
    
    
