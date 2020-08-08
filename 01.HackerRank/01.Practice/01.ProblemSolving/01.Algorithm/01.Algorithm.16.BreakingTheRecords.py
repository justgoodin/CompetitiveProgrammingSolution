#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minValue = maxValue = scores[0]
    minCount = maxCount = 0

    for value in scores:
        print(value,end=" ")
        if value>maxValue:
            maxCount += 1
            maxValue = value
        elif value<minValue:
            minCount += 1
            minValue = value
            
    return [maxCount,minCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()