f=1
for i in range(1,101):
    f*=i
ans=0
for i in str(f):
    ans+=ord(i)-48
print(ans)
    
