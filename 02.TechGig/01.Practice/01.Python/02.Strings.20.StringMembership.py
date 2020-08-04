'''
String Membership (100 Marks)
You just need to take string and a character as an input from stdin and print 'True' if that character is present in that string otherwise print 'False'.

Input Format
You will be taking a string and a character as an input from stdin.

Constraints
1 <= |S| <= 10000

Output Format
Print 'True' if that character is present in that string otherwise print 'False'.

Sample TestCase 1
Input
Hello Techgig
H
Output
True

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
    char = input()
  
    try:
        position = inputString.index(char)
        print("True",end="")
    except:
        print("False",end="")

main()