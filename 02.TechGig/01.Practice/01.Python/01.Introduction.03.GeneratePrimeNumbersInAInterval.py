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

'''
Generate Prime Numbers In A Interval (100 Marks)
You just need to take two number as input from stdin and you need to find prime numbers between those two numbers and print them.

Input Format
You will be taking two numbers as an input from stdin one on each line respectively.

Constraints
1 <= N <= 10000

Output Format
You need to print the prime numbers one on each line to the stdout.

Sample TestCase 1
Input
900
1000
Output
907
911
919
929
937
941
947
953
967
971
977
983
991
997

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB

Allowed Languages:
Python, Python 3
'''