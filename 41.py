import itertools

def prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def solve():
    num="7654321"
    for i in itertools.permutations(num):
        x="".join(i)
        x=int(x)
        #print(x)
        if prime(x):
            print(x)
            return

if __name__ == "__main__":
	(solve())
