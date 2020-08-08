#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'getTotalX' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def getTotalX(a, b):
    count = 0
    aSize = len(a)
    bSize = len(b)
    totalSize = aSize + bSize
    start = a[aSize-1]
    end = b[0]

    for i in range(start,end+1):
        flag = 0
        for j in a:
            if i%j==0:
                flag += 1
        for k in b:
            if k%i==0:
                flag += 1
        if flag == totalSize:
            count = count+1
            
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()