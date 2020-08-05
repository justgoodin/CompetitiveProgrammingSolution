#Link to the question below
#

n,m = map(int,input().strip().split(" "))
array = list(map(int,input().strip().split(" ")))
arrA = list(map(int,input().strip().split(" ")))
arrB = list(map(int,input().strip().split(" ")))

A = set(arrA)
B = set(arrB)

hA = [1 for i in array if set([i]).intersection(A)]  #Can be simpler logic, intent was to solve using sets
hB = [-1 for i in array if set([i]).intersection(B)] #Can be simpler logic, intent was to solve using sets

happiness = sum(hA) + sum(hB)

print(happiness)