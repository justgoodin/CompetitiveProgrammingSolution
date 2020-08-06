#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

def solve(meal_cost, tip, tax):
    output = round(meal_cost*(1+(tip+tax)/100))
    print(output)

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)