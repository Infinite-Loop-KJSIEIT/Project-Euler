import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())

ans=0
for i in range(1000):
    if i%3==0 or i%5==0:
        ans+=i
print(ans)
