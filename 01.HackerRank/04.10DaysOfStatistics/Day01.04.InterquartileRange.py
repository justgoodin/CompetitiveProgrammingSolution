def median(array):
    index = int(len(array)/2)
    #print(index)
    if (len(array))%2 ==0:
        output = float(array[index-1]+array[index])/2
    else:
        output = float(array[index])

    return [output,index,len(array)%2]

def interQuartile(array):
    
    Q2 = median(array)
    if len(array)%2==0:
        L = array[:Q2[1]]
        U = array[Q2[1]:]
    else:
        L = array[:Q2[1]-1]
        U = array[Q2[1]+1:]

    Q1 = median(L)
    Q3 = median(U)
    output = Q3[0] - Q1[0]

    return output


def main():
    n = int(input())
    X = list(map(int,input().split()))
    F = list(map(int,input().split()))
    array = []

    for f,x in zip(F,X):
        for i in range(f):
            array.append(x)

    array.sort()
    print(interQuartile(array))


main()


'''
Objective
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, , of  integers and an array, , representing the respective frequencies of 's elements, construct a data set, , where each  occurs at frequency . Then calculate and print 's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .

Constraints

, where  is the  element of array .
, where  is the  element of array .
The number of elements in  is equal to .
Output Format

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of  decimal place (i.e.,  format).

Sample Input

6
6 12 8 10 20 16
5 4 3 2 1 5
Sample Output

9.0
Explanation

The given data is:

InterquartileRange

First, we create data set  containing the data from set  at the respective frequencies specified by :
As there are an even number of data points in the original ordered data set, we will split this data set exactly in half:

Lower half (L): 6, 6, 6, 6, 6, 8, 8, 8, 10, 10

Upper half (U): 12, 12, 12, 12, 16, 16, 16, 16, 16, 20

Next, we find . There are  elements in  half, so  is the average of the middle two elements:  and . Thus, .

Next, we find .There are  elements in  half, so  is the average of the middle two elements:  and . Thus, .

From this, we calculate the interquartile range as  and print  as our answer.
'''
