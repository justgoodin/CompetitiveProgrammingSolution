#Link to the question below
#

def main():
    inputList = list(map(int,input().strip().split()))

    output = divmod(inputList[0],inputList[1])
    print(output)

main()