#Link to the question below
#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

#!/bin/python3

import sys


S = input().strip()

try:
    num = int(S)
    print(num)
except ValueError:
    print("Bad String")