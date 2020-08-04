'''
String isupper (100 Marks)
You just need to take string input from stdin and checks whether all the case-based characters (letters) of the string are uppercase.

Input Format
You will be taking a string as an input from stdin.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the boolean value(either True or False) to the stdout.

Sample TestCase 1
Input
This Is String Example
Output
False

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3
'''
def main():

    inputString = input()

    if inputString.isupper():
        print("True",end="")
    else:
        print("False",end="")

main()
