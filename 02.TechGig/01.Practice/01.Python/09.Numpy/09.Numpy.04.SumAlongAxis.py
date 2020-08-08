#Link to the question below
#https://www.techgig.com/practice/question/sum-alogn-axis/bm9vRzNrTGRlKy9EdlNRaDdPWSs2ck95Q055MjIrZEhEOGVBMFBOU1V4cUtYMlRkaDJha05qdHJudmpSb2Y2bg==/1

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
        output.append(sum(array[i,0:]))
        i += 1
    npOut = np.array(output)
    print(npOut)
main()