#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    yes = "YES"
    no = "NO"
    answer = str()

#Exception handling for cases where v1=v2, both can never meet as x1<x2  
    try:
        n = -(int(x2-x1))/(int(v2-v1))
    except:
        n = 0

    checkInt = n - int(n)

    if checkInt==0 and n>0:
        answer = yes
    else:
        answer = no

    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()