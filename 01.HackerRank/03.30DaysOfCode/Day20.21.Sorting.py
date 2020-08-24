#Link to the question below
#https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3
import sys

n = int(input().strip())
array = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0

for i in range(n):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            numSwaps += 1

print(f"Array is sorted in {numSwaps} swaps.")
print(f"First Element: {array[0]}")
print(f"Last Element: {array[-1]}")