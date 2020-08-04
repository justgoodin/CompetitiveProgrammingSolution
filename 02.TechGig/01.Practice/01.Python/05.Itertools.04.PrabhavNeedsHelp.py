'''
Prabhav Needs HELP (100 Marks)
Prabhav has been in a mental asylum for the last month. He was there for a survey. The asylum has a special way of letting people go. The asylum has asked Prabhav to tell all the combinations of a string upto size K in lexicographic order to be released. Prabhav is not good with Mathematics as you might have guessed. Can you help him get released ?

Input Format
The only line of input consist of string and size K space separately.

Constraints
1<= K <=|string|

Output Format
Print all combinations of string upto size K in lexicographic order.

Sample TestCase 1
Input
HELP 2

Output
E
H
L
P
EH
EL
EP
HL
HP
LP

'''
import itertools

def main():
    inputList, size = input().strip().split()
    size = int(size)
    flag = 0

    for i in range(0,size+1):
        for value in itertools.combinations(sorted(inputList),i):
            if flag ==0:
                flag =1
                continue
            else:
                print("".join(value))

main()