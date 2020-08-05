#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    counter = 1

    for i in range(0,n):
        for j in range(0,n-counter):
            print(end=" ")
        for k in range(0,counter):
            print("#",end="")
        
        counter += 1
        print()


if __name__ == '__main__':
    n = int(input())

    staircase(n)