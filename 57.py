'''
1 1/2
2 1/(2+1/2)=1/(2+last)=2/5
3 1/(2+1/(2+1/2))=1/(2+last)

new number can be writen as 1/(2+last_num/last_denom)
=last_denom/(2*last_denom+last_num)
'''
num=1
denom=2
ans=0
a=[]
for i in range(1000):
        if len(str(num+denom))>len(str(denom)):
                ans+=1
                #print(ans,num%10,denom%10)
        num,denom=denom,2*denom+num
print(ans)

