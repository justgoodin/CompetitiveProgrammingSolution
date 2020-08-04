'''
String upper (100 Marks)
You just need to take string input from STDIN and check whether all the case-based characters (letters) of the string are uppercase or not.

Input Format
You will be taking a string as an input from STDIN.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the Boolean value(either True or False) to the STDOUT.

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
    print(inputString.isupper(),end="")
main()
