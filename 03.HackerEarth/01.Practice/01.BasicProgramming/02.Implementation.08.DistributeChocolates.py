#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/distribute-chocolates-70c2c2ab/

import math
if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        c,n = map(int,input().split())

        k = math.floor((2*c - n*(n-1))/(2*n))
        if k<1:
            left = c
        else:
            left = int(c - n*(2*k + n - 1)//2)

        print(left)