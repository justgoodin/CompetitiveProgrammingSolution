#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = [0]*(max(ar)+1)
    counter=0

    for value in ar:
        count[value] +=1
    
    for value in count:
        counter += int(value/2)
    
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()