'''
Print Exact Slice Of String (100 Marks)
You need to take string input and two other numbers which will be the start and end point of the slice and you need to print that slice of string to the stdout.

Input Format
You will be taking a string as an input from stdin and two integers one on each line.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the slice of the string to the stdout.

Sample TestCase 1
Input
Hello Techgig
1
4
Output
ello
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
    inputRange = [int(input()),int(input())]

    print(inputString[inputRange[0]:inputRange[1]+1],end="")

main()