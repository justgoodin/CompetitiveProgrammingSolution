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



'''
Objective
In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Constraints

, where  is the  element of the array.
Output Format

Print  lines of output in the following order:

Print the mean on a new line, to a scale of  decimal place (i.e., , ).
Print the median on a new line, to a scale of  decimal place (i.e., , ).
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
Sample Output

43900.6
44627.5
4978
Explanation

Mean:
We sum all  elements in the array, divide the sum by , and print our result on a new line.

Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array . We then average the two middle elements:

and print our result on a new line.
Mode:
We can find the number of occurrences of all the elements in the array:

 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1
Every number occurs once, making  the maximum number of occurrences for any number in . Because we have multiple values to choose from, we want to select the smallest one, , and print it on a new line.
'''
