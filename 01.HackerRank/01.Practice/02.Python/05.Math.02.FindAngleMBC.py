import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())

    CA = (AB**2 + BC**2)**(1/2)

    DB = CA/2 #D being the mid point and not M, idiots

    #DB:DC::<DBC:<BCD
    #DB = DC, hence <DBC = <BCD 

    BCA = round(math.degrees(math.acos(BC/CA)))
	#Even better solution that doesn't require computing CA below
	#BCA = round(math.degrees(math.atan2(AB,BD)))
    print(str(BCA)+"°")


'''
 is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°
'''
