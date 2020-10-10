
a=1
b=2
ans=0
while a<=4000000:
    if a%2==0:
        ans+=a
    a,b=b,a+b
print(ans)
    
