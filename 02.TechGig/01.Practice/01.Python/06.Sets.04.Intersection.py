#Link to the question below
#https://www.techgig.com/practice/question/intersection/clk5djNTOXlpZm9BcjRxM1FOUXRFdjB6OU9uT25VZ1d5d1FJb0xMMk1ZblV5bVMzNE00TmJmOEdZZkxWQU92Kw==/1

def main():

    An = int(input())
    A = set(map(int,input().split()))
    Bn = int(input())
    B = set(map(int,input().split()))

    output = len(A.intersection(B))

    print(output)


main()