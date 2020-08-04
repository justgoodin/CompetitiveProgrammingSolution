def main():

        numTestCases = int(input())
        

        for i in range(0,numTestCases):
            numMembers = int(input())
            gRevolution = sorted(list(map(int,input().strip().split())))
            beyBlade = sorted(list(map(int,input().strip().split())))
            wins=0


            i,j = [0,0]


            while i<numMembers and j<numMembers:
                if gRevolution[i]>beyBlade[j]:
                    #print(gRevolution[i],end=" ")
                    #print(beyBlade[j])
                    #print(i,j)
                    wins+=1
                    i+=1
                    j+=1
                elif gRevolution[i]==beyBlade[j]:
                    i+=1
                else:
                    i+=1

            print(wins)

main()