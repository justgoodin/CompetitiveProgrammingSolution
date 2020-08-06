#Link to the question below
#

def main():

    count = int(input())
    inputList = [[]*4]*count
    sumOfScore = 0
    for i in range(0,count):
        inputList[i]=list(map(str,input().split(" ")))

    playerList = []
    
    for i in range(0,count):
        playerList.append(inputList[i][0])
     
    player = input()
    
    for  i in range(1,4):
        sumOfScore += int(inputList[playerList.index(player)][i])

    print('{:.2f}'.format(float(sumOfScore/3)))

main()