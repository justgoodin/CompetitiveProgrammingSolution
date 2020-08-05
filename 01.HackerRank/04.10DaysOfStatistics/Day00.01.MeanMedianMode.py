#Link to the question below
#

#import numpy as np
#import scipy as stats

#Solving without numpy and scipy
def mean(array):
    output = sum(array)/len(array)

    return output

def median(array):
    
    index = int(len(array)/2)-1
    output = (array[index]+array[index+1])/2
    return output

def mode(array):

    N = len(set(array))
    freqList = [list(set(array)),[0]*N]
    i = 0

    for item in array:
        if item in freqList[0]:
            freqList[1][freqList[0].index(item)] += 1

    maxFreq = max(freqList[1])
    finalList =[]

    for i in range(N):
        if freqList[1][i] == maxFreq:
            finalList.append(freqList[0][i])


    output = min(finalList)

    return output
    


def main():
    #Take input into an array
    N = int(input())
    array = list(map(int,input().strip().split()))
    #Sort the input based on one column
    array.sort()
    
    print(mean(array))
    print(median(array))
    print(mode(array))


main()