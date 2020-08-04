'''

'''
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def  decryptPassword(s):
    size = len(s)
    password = str()
    num = s.count('0')
    start = num
    i = num

    while i<size:
        if s[i].isupper() and s[i+1].islower():
            password += s[i+1]
            password += s[i]
            i = i + 3
        elif True:
            password += s[num-1]
            num -= 1
            i += 1
        else:
            password += s[i]
            i = i+1

    return password
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
