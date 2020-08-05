#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys
import itertools

# Not my best work, but they didn't allow me to import numpy
def migratoryBirds(arr):
    count = [0]*6
    for value in arr:
        count[value] += 1

    return count.index(max(count))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')
    fptr.close()