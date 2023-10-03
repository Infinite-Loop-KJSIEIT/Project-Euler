f=open('triangle.txt','r')
t=[]
for line in f:
    #print(line)
    t.append(list(map(int,line.split())))
for i in range(len(t)-2,-1,-1):
    for j in range(len(t[i])):
        t[i][j]+=max(t[i+1][j],t[i+1][j+1])
print(t[0][0])    
