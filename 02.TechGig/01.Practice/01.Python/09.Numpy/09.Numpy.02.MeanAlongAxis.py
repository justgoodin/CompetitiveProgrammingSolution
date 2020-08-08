#Link to the question below
#https://www.techgig.com/practice/question/mean-along-axis/RWEvYTM0RlNSZWpWcHJ4Nm9Kd2lzdFUrdTY4cW5jNXRRS2ppSU5MMVZMdmRpdlVrOWxhMTZDTi84YjVySnJaWg==/1

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
    while i<N:
        #print(i)
        output.append(sum(array[i,0:]/M))
        i += 1
    npOut = np.array(output)
    print(npOut)
main()