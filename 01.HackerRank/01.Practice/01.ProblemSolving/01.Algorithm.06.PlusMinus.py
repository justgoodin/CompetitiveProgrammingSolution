#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    size = len(arr)

    for value in arr:
        if value >0:
            positive += 1
        elif value <0:
            negative += 1
        else:
            zero += 1
    
    print(positive/size)
    print(negative/size)
    print(zero/size)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)