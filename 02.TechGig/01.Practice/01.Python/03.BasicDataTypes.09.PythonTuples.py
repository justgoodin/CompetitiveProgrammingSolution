#Link to the question below
#

def main():

    count = int(input())
    inputTuple = tuple(map(int,input().strip().split(" ")))
    pos = int(input())
    count = 0
    for i in inputTuple:
        if pos == i:
            count += 1

    print(count,end="")

main()