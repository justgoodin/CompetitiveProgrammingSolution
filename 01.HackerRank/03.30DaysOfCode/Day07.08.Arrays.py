#Link to the question below
#https://www.hackerrank.com/challenges/30-arrays/

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    print(" ".join(str(i) for i in arr[::-1]))

