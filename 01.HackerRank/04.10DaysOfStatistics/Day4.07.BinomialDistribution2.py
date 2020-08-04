def fact(n):
    return n*fact(n-1) if n>1 else 1

def nCr(n,r):
    return int(fact(n)/(fact(n-r)*fact(r)))

if __name__ == "__main__":
    d,n = map(int,input().split())
    pd = d/100
    x = 2
    pe = 1-pd
    p2e = 0
    p2d = 0

    for r in range(n-x,n+1):
        p2e += round((nCr(n,r)*((pe)**r)*((1-pe)**(n-r))),4)

    for r in range(x,n+1):
        p2d += round((nCr(n,r)*((pd)**r)*((1-pd)**(n-r))),4)

    print(round(p2e,3))
    print(round(p2d,3))

    
    
'''
answer
0.891
0.342
'''
'''
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

No more than  rejects?
At least  rejects?
Input Format

A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

12 10
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the answer to each question on its own line:

The first line should contain the probability that a batch of  pistons will contain no more than  rejects.
The second line should contain the probability that a batch of  pistons will contain at least  rejects.
Round both of your answers to a scale of  decimal places (i.e.,  format).
'''
