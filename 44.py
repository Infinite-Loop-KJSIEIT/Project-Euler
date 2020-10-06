import itertools
import math
import time

def check(n):
    N=(math.sqrt(1+24*n)+1)/6
    return N==math.floor(N)        

def solve():
    for i in range(1,10**6):
        n1=i*(3*i-1)//2
        for j in range(i-1,0,-1):
            n2=j*(3*j-1)//2
            if check(n1-n2) and check(n1+n2):
                print(n1,n2)
                print(n1-n2)
                return

if __name__ == "__main__":
    st=time.time()
    (solve())
    print(time.time()-st,"S")
