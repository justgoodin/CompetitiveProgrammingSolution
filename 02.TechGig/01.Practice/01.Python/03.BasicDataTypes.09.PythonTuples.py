def main():

    count = int(input())
    inputTuple = tuple(map(int,input().strip().split(" ")))
    pos = int(input())
    count = 0
    for i in inputTuple:
        if pos == i:
            count += 1

    print(count,end="")

main()

'''
Python-Tuples (100 Marks)
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
You are given N Integers. Your task is to create a tuple and insert all the given integers into it.
After insertion, You have to print the count of a particular element X (total number of occurrence of that element) in the tuple.

Input Format
First Line will contain an Integer N, denoting the number of elements to be inserted into the tuple.
Next Line contains N integers.
Next Line will contain an Integer X.

Constraints
1 <= N <= 10^3

Output Format
You have to print the count of element X in the tuple.

Sample TestCase 1
Input
4
1 3 3 5
3
Output
2

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''
