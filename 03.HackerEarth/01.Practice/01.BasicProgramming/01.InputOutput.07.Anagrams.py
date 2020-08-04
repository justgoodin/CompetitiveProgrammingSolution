import math 

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        string1 = list(input())
        string2 = list(input())
        total = string1+string2
        word1 = set(string1)
        word2 = set(string2)
        count=0
        
        for j in set(total):
            count += abs(string1.count(j)-string2.count(j))
            
        print(count)


'''
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

Desired O/p

Constraints :

string lengths<=10000

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.

SAMPLE INPUT 
1
cde
abc
SAMPLE OUTPUT 
4
'''
