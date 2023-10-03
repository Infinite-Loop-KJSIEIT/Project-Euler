# from decimal import Decimal
import collections as coll
import sys
import math as mt

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
t = []
n = int(input())
for i in range(n):
    t.append(list(tres()))
ans = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, len(t[i - 1]) + 1):
        ans[i][j] = max(
            t[i - 1][j - 1] + ans[i - 1][j], t[i - 1][j - 1] + ans[i - 1][j - 1]
        )
print(max(ans[-1]))

# End Time
time2 = time.time()
print("Time Taken:", (time2 - time1) * 1000)
