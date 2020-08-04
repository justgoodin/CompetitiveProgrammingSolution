def median(array):
    #array.sort()
    index = int(len(array)/2)
    if (len(array))%2 ==0:
        output = int((array[index-1]+array[index])/2)
        #print(index,output)
    else:
        output = array[index]

    return output

def quartile(array, Qn):
    output = [0]*3
    output[1] = median(array)
    output[0] = median([i for i in array if i<output[1]])
    output[2] = median([i for i in array if i>output[1]])

    return output[Qn-1]


def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))   

    print(quartile(array,1))
    print(quartile(array,2))
    print(quartile(array,3))

main()


'''
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Constraints

, where  is the  element of the array.
Output Format

Print  lines of output in the following order:

The first line should be the value of .
The second line should be the value of .
The third line should be the value of .
Sample Input

9
3 7 8 5 12 14 21 13 18
Sample Output

6
12
16
Explanation

. When we sort the elements in non-decreasing order, we get . It's easy to see that .

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

Lower half (L): 3, 5, 7, 8

Upper half (U): 13, 14, 18, 21

Now, we find the quartiles:

 is the . So, .
 is the . So, .
 is the . So, .
'''
