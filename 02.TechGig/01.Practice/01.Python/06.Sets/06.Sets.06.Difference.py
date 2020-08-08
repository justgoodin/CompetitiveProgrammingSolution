#Link to the question below
#https://www.techgig.com/practice/question/difference/RFREbmV5cVJiL2wxcDk2aVphU3RaUnFRd0p6amlURGRKZjRoWUVaTXdpQ1lhdFpnSUpRZzVWRzBDUjk3OE5LbQ==/1

def main():

    An = int(input())
    A = set(map(int,input().split()))
    Bn = int(input())
    B = set(map(int,input().split()))

    output = A.symmetric_difference(B)

    for item in output:
        print(item)

main()