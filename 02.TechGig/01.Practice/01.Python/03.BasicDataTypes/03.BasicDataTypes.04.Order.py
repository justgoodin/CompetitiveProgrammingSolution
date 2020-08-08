#Link to the question below
#

def main():

    count = int(input())
    inputList = []

    for i in range(0,count):
        inputList.append((input()))

    sortedList = sorted(inputList)

    for i in range(0, count):
        print(sortedList[i])

main()