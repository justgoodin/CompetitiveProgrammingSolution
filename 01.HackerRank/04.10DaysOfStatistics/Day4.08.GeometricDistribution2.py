def fact(n):
    return n*fact(n-1) if n>1 else 1

def nCr(n,r):
    return int(fact(n)/(fact(n-r)*fact(r)))

if __name__ == "__main__":
    numerator, denominator = map(int,input().split())
    n = int(input())
    p = numerator/denominator
    x = 1
    output = 0
    for i in range(1,n+1):
        output += round(nCr(i-1,x-1)*(p**x)*((1-p)**(i-x)),4)
    
    print(round(output,3))



    
'''
Objective
In this challenge, we go further with geometric distributions. We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task
The probability that a machine produces a defective product is . What is the probability that the  defect is found during the first  inspections?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of the first defect being discovered by:

1 3
5
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
'''
