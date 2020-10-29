ans=0
for i in range (1,10):
    p=1
    while True:
        if len(str(i**p))==p:
            print(i,p)
            ans+=1
        else:
            break
        p+=1
print(ans)
