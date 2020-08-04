'''
String Repetition (100 Marks)
You just need to take a string and a integer as an input from stdin and repeat the string up to the count given as in integer.

Input Format
You will be taking a string and an integer as an input from stdin.

Constraints
1 <= |S| <= 1000
1 <= N <= 100

Output Format
You need to print the string to the stdout.

Sample TestCase 1
Input
Hello
2
Output
HelloHello

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
    num = int(input())

    for i in range(0,num):
        print(inputString,end="")

main()
