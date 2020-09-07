#Link to the question below
#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

import itertools

string, n = map(str,input().split())
n = int(n)

tempList = []

for item in itertools.combinations_with_replacement(string,n):
    tempStr = "".join(sorted(item))
    tempList.append(tempStr)

tempList.sort()
for item in tempList:
    print(item)