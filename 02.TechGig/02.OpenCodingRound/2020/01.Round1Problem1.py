''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    numOfIngred = int(input())
    quantRequired = list(map(int,(input().strip().split(" "))))
    quantAvailable = list(map(int,input().strip().split(" ")))
    quant = sorted([a/b for a,b in zip(quantAvailable,quantRequired)])
      
    print(int(quant[0]))

main()