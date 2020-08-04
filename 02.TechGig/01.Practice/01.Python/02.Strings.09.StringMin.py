'''
String minimum (100 Marks)
You just need to take string input from STDIN and print the min alphabetical character from the string.

Input Format
You will be taking a string as an input from STDIN. 

Constraints
1 <= |S| <= 10000

Output Format
You need to print the min alphabetical character from the string to the STDOUT. 

Sample TestCase 1
Input
why i am
Output
a

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
    """inputString = (min(input().replace(" ","").strip()))
    
    print(inputString)
    for i in inputString:
        if i.isalpha()==True:
            print(i,end="")
            break
    """
    x = input()
    y=min(x.lower().replace(" ",""))
    z =min(x.replace(" ",""))

    if y<z.lower():
        print(y,end="")
    else:
        print(z,end="")

main()