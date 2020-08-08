#Link to the question below
#https://www.techgig.com/practice/question/product-of-sum/OTcvRHQzZW01ZFViUk9nMTc2dkxhYWwwTWlGeGs3RnNiL0o2SGQyemJmYmhKb2NJWjRQUUdwTFFJZkVWMTNIYg==/1

import numpy as np

def main():
    N,M = map(int,input().split())
    listArray = [[]*N]*M
    #array  = np.array(N*M)

    for i in range(N):
        listArray[i] = list(map(int,input().split()))
    output = 0
    array = np.array(listArray)
    output = []
    i = 0
    product = 1
    while i<N:
        #print(i)
        product *= sum(array[i,0:])
        i += 1
    
    print(product)
main()