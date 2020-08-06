#Link to the question below
#

def main():
    numberList = [int(input()),int(input())]
    countPrime = 0
    primeList = list()
    
    for i in range(numberList[0],numberList[1]):
        if checkPrime(i)==1:
            primeList.append(i)
            countPrime=countPrime+1
        
    for i in primeList:
        print(i,end="")
        if i==primeList[len(primeList)-1]:
            print(end="")
        else:
            print()
        
def checkPrime(num):
    isPrime = 1
    for i in range(2,num-1):
        if (num%i==0):
            isPrime = 0
    return isPrime

main()