'''
Cartesian Product (100 Marks)
Aahan has provided you two list X and Y. He needs you to find the cartesian product X *  Y for him.

Input Format
The first line of input consist of elements of X space separately.
The second line of input consist of elements of Y separately.

Constraints
1<= X <=10
1<= Y <=10

Output Format
Print the cartesian product X * Y

Sample TestCase 1
Input
2 4
3 5

Output
(2, 3) (2, 5) (4, 3) (4, 5)

'''
import itertools

def main():

    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))

    C = list(itertools.product(A,B))

    for i in range(0,len(C)):
        if i==len(C)-1:
            print(C[i])
        else:
            print(C[i],end=" ")

main()


