#Link to the question below
#

import itertools

def main():
    inputList, size = input().strip().split()
    size = int(size)
    flag = 0

    for i in range(0,size+1):
        for value in itertools.combinations(sorted(inputList),i):
            if flag ==0:
                flag =1
                continue
            else:
                print("".join(value))

main()