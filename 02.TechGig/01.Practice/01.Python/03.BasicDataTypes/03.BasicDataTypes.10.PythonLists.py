#Link to the question below
#

def main():

    count = int(input()) 
    ansList = [] 

    isPass1 = True 
    
    for i in range(count): 
        x = input().strip().split() 

        if x[0]=='1': 
            ansList.append(x[1]) 
        elif x[0]=='2': 
            if isPass1: 
                isPass1 = False 
            else: 
                print() 
            print(ansList, end="")

main()