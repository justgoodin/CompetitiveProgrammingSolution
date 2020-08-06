#Link to the question below
#

import itertools

def main():
    inputString = input().strip()
    inputList = sorted(inputString)
    length = len(set(inputString))
    

    for key, value in itertools.groupby(inputList):
        print((len(list(value)), key), end="")
        if length > 1:
            print(end=" ")
            length -=1
        else:
            print(end="")

main()