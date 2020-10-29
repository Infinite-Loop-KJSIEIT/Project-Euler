import time
st=time.time()

m=0
for i in range(100):
    for j in range(100):
        s=str(i**j)
        m=max(m,sum(int(d) for d in s))
print(m)
print(time.time()-st,"s")

st=time.time()
print(max(sum(int(c) for c in str(a**b))
		for a in range(100) for b in range(100)))
print(time.time()-st,"s")
