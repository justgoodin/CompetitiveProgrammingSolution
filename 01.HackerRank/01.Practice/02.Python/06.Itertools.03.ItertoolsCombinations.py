#Link to the question below
#https://www.hackerrank.com/challenges/itertools-combinations/problem

import itertools

string, n = map(str,input().split())
n = int(n)

stringList = []

for i in range(1,n+1):
    tempList = []
    for item in itertools.combinations(string,i):
        tempStr = "".join(sorted(item))
        tempList.append(tempStr)

    tempList.sort()
    for item in tempList:
        print(item)