from math import sqrt

x, i = 600851475143, 2
while i * i <= x:
    while x % i == 0 and x != i:
        x //= i
    i += 1
print(x)
