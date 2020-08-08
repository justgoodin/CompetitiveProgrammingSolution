#Link to the question below
#

def main():

    inputList = list(map(int,input().strip().split()))
    output = inputList[0]**inputList[1]%inputList[2]

    print(output)

main()