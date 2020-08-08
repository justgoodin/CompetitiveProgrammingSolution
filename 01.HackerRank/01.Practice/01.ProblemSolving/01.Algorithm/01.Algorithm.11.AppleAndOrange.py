#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    countApple = 0
    countOrange = 0

    for d in apples:
        if a+d>=s and a+d<=t:
            countApple += 1
    
    for d in oranges:
        if b+d<=t and b+d>=s:
            countOrange += 1

    print(countApple)
    print(countOrange)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)