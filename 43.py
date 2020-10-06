import itertools

def check(n):
    return all((int(num[i + 1]) * 100 + int(num[i + 2]) * 10 + int(num[i + 3])) % p == 0
               for (i, p) in enumerate(DIVISIBILITY_TESTS))
    
DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]
s="0123456789"
ans=0
for num in itertools.permutations(s):
    if check(num):
        ans+=int("".join(num))
print(ans)
