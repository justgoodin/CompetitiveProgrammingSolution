def main():

    count = int(input()) 
    ansList = [] 

    isPass1 = True 
    
    for i in range(count): 
        x = input().strip().split() 

        if x[0]=='1': 
            ansList.append(x[1]) 
        elif x[0]=='2': 
            if isPass1: 
                isPass1 = False 
            else: 
                print() 
            print(ansList, end="")

main()

'''
Python Lists (100 Marks)
List is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
Your task is to maintain a list and perform two types of queries on it : 
Query '1' : It will be given as 1 x  : Insert x into the list.
Query '2' : It will be given as 2 : Print the contents of the list.

Input Format
First line will contain an Integer Q, denoting the number of Queries.
Next Q lines contains an Integer denoting query type.
Type 1 Query is followed by a data item (integer or a sting) which is to be inserted into the list.

Constraints
1 <= Q <= 10^3

Output Format
For each type 2 query, print the contents of the list in new line.

Sample TestCase 1
Input
5
1 32
2
1 arpit
1 54
2

Output
['32']
['32', 'arpit', '54']
Time Limit(X):
1.00 sec(s) for each input.

Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''