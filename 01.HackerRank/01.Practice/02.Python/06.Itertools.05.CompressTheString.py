#Link to the question below
#https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools

inputStr = input()

for key, value in itertools.groupby(inputStr,key=lambda x: x[0]):
    print(f"({len(list(value))}, {key})",end=" ")