#Link to the question below
#

N = input() #useless info TBH

array = set()
count = 0

try:
    while True:
        array.add(input())
except:
    count = len(array)

print(count)