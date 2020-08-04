'''
RUBY and String (100 Marks)
Ruby has a string of characters with her. She needs to group the characters of the string and present it to her teacher. Can you help her with grouping ?

Input Format
The only line of input consist of string of characters

Constraints
1<= |string| <=25

Output Format
Print the grouped characters in their original order space separately.

Sample TestCase 1
Input
aabbccc

Output
(2, 'a') (2, 'b') (3, 'c')

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
            print()

main()

