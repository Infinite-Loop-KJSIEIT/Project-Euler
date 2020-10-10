import itertools

a=[0,1,2,3,4,5,6,7,8,9]
p=itertools.permutations(a)
per=itertools.islice(p,999999, None)
print("".join(str(x) for x in next(per)))


