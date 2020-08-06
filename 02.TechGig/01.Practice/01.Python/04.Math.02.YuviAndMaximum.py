#Link to the question below
#

def main():
    inputList = sorted(list(map(int,input().strip().split(" "))),reverse=True)
    print(inputList[0]+inputList[1])

main()