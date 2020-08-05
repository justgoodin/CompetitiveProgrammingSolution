#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice, bob = 0,0

    for i,j in zip(a,b):
        if i>j:
            alice += 1
        elif i<j:
            bob += 1
    
    return list([alice,bob])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()