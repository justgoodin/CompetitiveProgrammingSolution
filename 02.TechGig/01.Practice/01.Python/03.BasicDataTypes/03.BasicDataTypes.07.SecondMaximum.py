#Link to the question below
#

def main():

    count = int(input())
    marksList = sorted(list(map(int,(input().strip().split(" ")))),reverse=True)
    secLowest = marksList[0]

    for i in range(1,count):
        secLowest = marksList[i]
        if secLowest ==marksList[i-1]:
            continue
        else:
            break

    print(secLowest)    

main()