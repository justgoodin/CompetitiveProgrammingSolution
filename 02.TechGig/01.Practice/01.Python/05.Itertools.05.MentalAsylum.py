'''
Mental Asylum (100 Marks)
One of the patients in mental asylum wants to give test to get released. The asylum has asked him the problem similar to PRABHAV but with replacements allowed. The duplicates are allowed in this case. Help the patient to get released.

Note: Solve problem PRABHAV NEEDS HELP before solving this problem.

Input Format
The only line of input consist of string and size M space separately.

Constraints
1<= M <=5

Output Format
Print all the combinations of string of size M lexicographically with replacements allowed.

Sample TestCase 1
Input
HELP 2

Output
EE
EH
EL
EP
HH
HL
HP
LL
LP
PP
'''

import itertools

def main():
    inputString, size = input().strip().split()
    size = int(size)
    inputList = list(itertools.permutations(sorted(inputString),size))
    for value in inputList:
        print("".join(value))

main()
