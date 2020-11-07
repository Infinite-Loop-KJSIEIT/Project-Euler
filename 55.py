
import time
st=time.time()
count=0
for i in range(1,10**4):
    num=i+int(str(i)[::-1])
    c=0
    
    while str(num)!=str(num)[::-1] and c<25:
        c+=1
        num=num+int(str(num)[::-1])
        
    if c==25:
        #print(i,num)
        count+=1
print(count)
print(time.time()-st,'s')


