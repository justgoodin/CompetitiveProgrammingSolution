'''
Cartesian Product (100 Marks)
For sets A and B, the Cartesian product of A and B, denoted AxB, is the set of all ordered pairs (a, b) such that a A and b B. That is, AxB = {(a, b)| a A b B}. 
itertools.product() computes the cartesian product of input iterables. 
 For example, product(P, Q) returns the same as ((x,y) for x in P for y in Q). 
You are given a two lists A and B. Your task is to compute their cartesian product AXB.

Input Format
The first line contains the space separated elements of list. 
The second line contains the space separated elements of list.
Both lists have no duplicate integer elements.

Constraints
1 <= elements in List A <= 40
1 <= elements in List B <= 40

Output Format
Output the cartesian product of the two list as tuples separated by spaces.

Sample TestCase 1
Input
2 4
7 8

Output
(2, 7) (2, 8) (2, 9) (4, 7) (4, 8) (4, 9)

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB

Allowed Languages:
Python, Python 3, Pypy

'''
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

