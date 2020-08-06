#Link to the question below
#

import itertools

def main():

    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))

    C = list(itertools.product(A,B))

    for i in range(0,len(C)):
        if i==len(C)-1:
            print(C[i])
        else:
            print(C[i],end=" ")

main()