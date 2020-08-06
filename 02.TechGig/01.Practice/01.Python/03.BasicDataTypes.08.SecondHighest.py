#Link to the question below
#

def main():

    count = int(input())

    names = []
    marks = []
    finalList = []
    for i in range(0,count):
        names.append(input())
        marks.append(int(input()))

        sortedMarks = sorted(marks,reverse=True)
        second = 0
    for i in range(1,count):
        second = sortedMarks[1]
        if second > sortedMarks[i]:
            continue
        else: 
            break
        
    for i in range(count):
        if marks[i]==second:
            finalList.append(names[i].strip())

    sortedList = sorted(finalList)

    for i in range(len(sortedList)):
        print(sortedList[i],end="")
        if i < len(sortedList)-1:
            print()

main()