import math

def main():

    AB = int(input())
    BC = int(input())

    CA = (AB**2+BC**2)**(1/2)
    AD = CA/2

    aBCA =  round(math.degrees(math.asin(BC/CA)))

    print(aBCA,end="")

main()
'''
Find Angle (100 Marks)
Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
You will be given two integers denoting sides AB and BC respectively.
Round off your answer to the nearest Integer.

Input Format
First line will contain an Integer denoting side AB.
Second line will contain an Integer denoting side BC.

Constraints
1 <= side AB <= 200
1 <= side BC <= 200

Output Format
Output Angle ABD, rounded off to nearest integer.

Sample TestCase 1
Input
6
6
Output
45
Explanation

Angle ABD = 45 degrees.
Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''