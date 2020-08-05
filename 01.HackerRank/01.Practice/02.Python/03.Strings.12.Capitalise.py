#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

def solve(s):
    listString = s.split(' ')
    string= str()
    
    string = ' '.join((word.capitalize() for word in listString))
        
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()