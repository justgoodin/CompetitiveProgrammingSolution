#Link to the question below
#

import itertools

def main():
    inputString, size = input().strip().split()
    size = int(size)
    inputList = list(itertools.permutations(sorted(inputString),size))
    for value in inputList:
        print("".join(value))

main()