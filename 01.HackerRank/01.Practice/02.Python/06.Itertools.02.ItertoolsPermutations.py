#Link to the question below
#https://www.hackerrank.com/challenges/itertools-permutations/problem

import itertools

string, n = map(str,input().split())
n = int(n)

stringList = []

for item in itertools.permutations(string,n):
    stringList.append("".join(item))

stringList.sort()

for item in stringList:
    print(item)