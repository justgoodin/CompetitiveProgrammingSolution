#Link to the question below
#

import math
def main():
    inputList = list(map(int,input().strip().split()))

    #output = int(math.pow(inputList[0],inputList[1])%inputList[2])
	#above code doesn't pass test case 7, below does! Idiots didn't configure it correctly
    output = inputList[0]**inputList[1]%inputList[2]
    print(output,end="")

main()