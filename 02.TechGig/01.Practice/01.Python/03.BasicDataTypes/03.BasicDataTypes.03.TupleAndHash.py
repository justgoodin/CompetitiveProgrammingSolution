#Link to the question below
#

def main():
    
    count = int(input())
    inputList = list(map(int,input().split(" ")))
    
    inputTuple = tuple(inputList)

    print(hash(inputTuple))

main()