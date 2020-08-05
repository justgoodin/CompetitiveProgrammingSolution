#Link to the question below
#

m = int(input())
mArray = list(map(int,input().strip().split(" ")))
n = int(input())
nArray = list(map(int,input().strip().split(" ")))

diff = set(mArray).symmetric_difference(set(nArray))
ldiff = sorted(diff)

for value in ldiff:
    print(value)