#Link to the question below
#

def main():

    count = int(input())
    inputList = list(map(int,input().strip().split()))
    sum =0

    for i in range(0,count):
        if inputList[i]%2 == 0:
            sum += inputList[i]

    print(sum)

main()