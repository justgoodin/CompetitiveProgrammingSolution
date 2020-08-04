'''
String join (100 Marks)
You just need to take string input from stdin and bunch from strings one on each line and you need to concatenate them as shown in the sample.

Input Format
You will be taking strings as an input from stdin one on each line respectively.

Constraints
1 <= |S| <= 10000

Output Format
You need to print the string after concatenation to the stdout.

Sample TestCase 1
Input
-
a
b
c
Output
a-b-c

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

    separator = input()
    inputString = []
    
    while(True):
        try:
            ch=input()
        except:
            break;
        inputString.append(ch)

    outputString = separator.join(inputString)

    print(outputString,end="")

main()

