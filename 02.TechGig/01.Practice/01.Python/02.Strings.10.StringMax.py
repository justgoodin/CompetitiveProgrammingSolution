'''
String max (100 Marks)
You just need to take string input from stdin and print the max alphabetical character from the string.

Input Format
You will be taking a string as an input from stdin.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the max alphabetical character from the string to the stdout.

Sample TestCase 1
Input
why i am
Output
y

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
	inputString=(input().strip())
	maxValue=max(inputString)
	print(maxValue,end="")
main()