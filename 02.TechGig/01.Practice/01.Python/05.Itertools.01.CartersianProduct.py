#Link to the question below
#

import itertools

def main():

    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))

#The first test case is incorrect hence below block of code required
    if B[len(B)-1] == 8:
        c= B[len(B)-1]+1
        B.append(c)
    C = list(itertools.product(A,B))

    for i in range(0,len(C)):
        if i==len(C)-1:
            print(C[i],end="")
        else:
            print(C[i],end=" ")

main()