'''

'''
#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'getBattery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY events as parameter.
#

def getBattery(events):
    charge = 50
    for i in events:
        charge = charge + i
        if charge >= 100:
            charge = 100
    
    return charge


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    result = getBattery(events)

    fptr.write(str(result) + '\n')

    fptr.close()