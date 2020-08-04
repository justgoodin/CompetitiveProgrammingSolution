'''
Decompress String (100 Marks)
You are given a string S. You to have to first sort the characters in the string. Now, Suppose a character 'c' occurs x times in the  modified string. 
Replace these consecutive occurrences of the character 'c' with (x, c) in the string.
Itertools.groupby() will help you in achieving it.

Input Format
First line will contain a string s.

Constraints
2 <= |s| <= 10^3

Output Format
A single line containing the modified string. 

Sample TestCase 1
Input
aaabbcccd
Output
(3, 'a') (2, 'b') (3, 'c') (1, 'd')
'''
import itertools

def main():
    inputString = input().strip()
    inputList = sorted(inputString)
    length = len(set(inputString))
    

    for key, value in itertools.groupby(inputList):
        print((len(list(value)), key), end="")
        if length > 1:
            print(end=" ")
            length -=1
        else:
            print(end="")

main()

