import math
n=2000000
a=[0]*(n)
i=2
while i<n:
    #print(a,i)
    if a[i]==0:
        j=2
        while i*j<n:
            a[i*j]=1
            j+=1
    i+=1
ans=0
for i in range(2,n):
    if a[i]==0:
        ans+=i
print(ans)
        
            
            
    
        
        
        
                      
        

    
