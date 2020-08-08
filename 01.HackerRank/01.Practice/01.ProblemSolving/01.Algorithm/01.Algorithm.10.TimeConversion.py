#Link to the question below
#

#!/bin/python3
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    size = len(s)
    newTime = str()
    clock = s[size-2:]

    if s[0:2] == "12" and clock =="AM":
        newTime= "00" + s[2:size-2]
    elif s[0:2] == "12" and clock =="PM":
        newTime = s[:size-2]
    elif clock == "AM":
        newTime += s[:size-2]
    elif clock == "PM":
        newTime = str(int(s[0:2])+12)+ s[2:size-2]
    
    return newTime

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()