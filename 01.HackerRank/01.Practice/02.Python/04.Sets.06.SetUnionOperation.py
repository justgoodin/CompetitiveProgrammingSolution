#Link to the question below
#

n = int(input()) #Redundant in python
english = set(map(int,input().strip().split()))
b = int(input()) #Redundant in python
french = set(map(int,input().strip().split()))

sub = english.union(french)

print(len(sub))