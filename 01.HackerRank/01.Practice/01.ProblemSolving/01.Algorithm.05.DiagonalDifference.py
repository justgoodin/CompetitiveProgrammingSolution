#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sumOfArr = 0
    size = len(arr)-1
    i = 0
    while i<=size:
        sumOfArr = sumOfArr + (arr[i][i]-arr[size-i][i])
        i += 1
    
    return abs(sumOfArr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()