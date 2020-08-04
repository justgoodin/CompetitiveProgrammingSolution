'''
Group Consecutive (100 Marks)
There is a string provided to you. In the string there may or may not be consecutive duplicates. You have to duplicate all the characters of the strings with their consecutive occurrences.
Grouping should be done in order (occurrences, character).

Input Format
The only line of input consist of string.

Constraints
1<= |string| <=25

Output Format
Print all the characters of the strings grouped by their consecutive occurrences.

Sample TestCase 1
Input
244001

Output
(1, 2) (2, 4) (2, 0) (1, 1)


'''
import itertools

def main():
    inputString = input().strip()
    inputList = inputString
    length = len(set(inputString))
    

    for key, value in itertools.groupby(inputList):
        print((len(list(value)), int(key)), end="")
        if length > 1:
            print(end=" ")
            length -=1
        else:
            print()

main()