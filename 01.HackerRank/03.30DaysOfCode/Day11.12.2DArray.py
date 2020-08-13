#Link to the question below
#https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    maxHG = -9*6 # Negative values of A[i][j] screws up the check of largest sum later
    for i in range(0,4):
        for j in range(0,4):
            sumOfHG =  sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            
            if sumOfHG > maxHG:
                maxHG = sumOfHG
                #print(arr[i][j:j+3])
                #print(arr[i+1][j+1])
    
    print(maxHG)