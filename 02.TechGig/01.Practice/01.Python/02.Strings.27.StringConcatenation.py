'''
String Concatenation (100 Marks)
You just need to take two strings as input from stdin and concatenate them and print the concatenated string to the stdout.

Input Format
You will be taking two strings as an input from stdin one on each line respectively.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the concatenated string to the stdout.

Sample TestCase 1
Input
Hello 
Techgig
Output
HelloTechgig

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

    inputString1 = input()
    inputString2 = input()
    inputString3 = "".join([inputString1.strip(),inputString2.strip()])

    print(inputString3,end="")

main()