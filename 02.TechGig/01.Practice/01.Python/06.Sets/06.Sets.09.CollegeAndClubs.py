#Link to the question below
#https://www.techgig.com/practice/question/college-and-clubs/bE16S2M4YXNiYWxNSGovWnNoSWJkbmRuVHVmT2JtMW9tY3UwMGYrSzZrelk3NmhGMkZwc3ZCRWhzMzNPMWcvdw==/1

def main():

    An = int(input())
    A = set(map(int,input().split()))
    Bn = int(input())
    B = set(map(int,input().split()))

    output = len(A.union(B))

#Stupidity ensues below
    print(output,end="")

main()

