# from decimal import Decimal
import collections as coll
import math as mt
import sys
# import random as rd
# import bisect as bi
import time

sys.setrecursionlimit(1000000)

# import numpy as np


def uno():
    return int(sys.stdin.readline().strip())


def dos():
    return sys.stdin.readline().strip()


def tres():
    return map(int, sys.stdin.readline().strip().split())


def cuatro():
    return sys.stdin.readline().strip().split()


# Starting Time
time1 = time.time()


######## CODE STARTS FROM HERE ########
n = uno()
ans = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        ans += i
print(ans)

# End Time
time2 = time.time()
# print("Time Taken:", (time2 - time1) * 1000)
