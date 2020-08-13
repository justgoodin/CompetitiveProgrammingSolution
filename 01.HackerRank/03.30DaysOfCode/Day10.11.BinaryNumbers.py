#Link to the question below
#https://www.hackerrank.com/challenges/30-binary-numbers/

#!/bin/python3
import math
import os
import random
import re
import sys

def maxConsec(string):
    pattern=re.findall(r"1*",string)
    pattern.sort(reverse=True)
    return len(pattern[0])


if __name__ == '__main__':
    decN = int(input())
    binN = bin(decN)
    stringN = str(binN)[2:]

    print(maxConsec(stringN))