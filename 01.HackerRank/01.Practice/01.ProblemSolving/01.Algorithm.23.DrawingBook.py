#Link to the question below
#

#!/bin/python3
import os
import sys

def pageCount(n, p):
    mid = int(n/2)
    pages = 0

    if p<= mid:
        pages = int((p/2))
    else:
        if n%2 == 0:
            pages = int((n-p+1)/2)
        else: 
            pages = int((n-p)/2)
    
    return pages

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')
    fptr.close()