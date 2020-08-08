#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    total = sum(bill)
    b_actual = int((total - bill[k])/2)

    if b == b_actual:
        print("Bon Appetit")
    else:
        print(b-b_actual)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)