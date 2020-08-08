#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ascending = sorted(arr,reverse=True)
    descending = sorted(arr)
    size = len(arr)-1
    maximum,minimum = 0,0

    for i in range(0,size):
        maximum += ascending[i]
        minimum += descending[i]
    
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)