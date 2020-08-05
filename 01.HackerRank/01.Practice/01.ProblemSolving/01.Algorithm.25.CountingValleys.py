#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

def countingValleys(n, steps):
    level = 0
    valley = 0

    for step in steps:
        if step =="D":
            level -= 1
        else:
            level += 1

        print(level)
        if step=="U" and level ==0:
            valley +=1
    
    return (valley)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')
    fptr.close()