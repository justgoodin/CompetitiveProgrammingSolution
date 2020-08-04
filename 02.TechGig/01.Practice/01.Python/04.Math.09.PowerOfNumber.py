import math
def main():
    inputList = list(map(int,input().strip().split()))

    #output = int(math.pow(inputList[0],inputList[1])%inputList[2])
	#above code doesn't pass test case 7, below does! Idiots didn't configure it correctly
    output = inputList[0]**inputList[1]%inputList[2]
    print(output,end="")

main()

'''
Power of a Number (100 Marks)
Python.math module provides access to the mathematical functions defined by the C standard.
One of the widely used function is math.pow(x, y) which Returns x raised to the power y.
Now, you are given three integers x, y and M. You have to print ( x ^ y ) Mod M.

Input Format
First line will contain three integers x, y, and M.

Constraints
1 <= X <= 20
1 <= Y <= 100
2 <= M <= 100

Output Format
Print an Integer denoting answer of the calculation (x ^ y ) Mod M.

Sample TestCase 1
Input
10 2 3
Output
1
Explanation
10^2 = 100

100 % 3 = 1
Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''