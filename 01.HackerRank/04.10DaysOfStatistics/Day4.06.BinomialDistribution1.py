def fact(n):
    return n*fact(n-1) if n>1 else 1

def nCr(n,r):
    return int(fact(n)/(fact(n-r)*fact(r)))

if __name__ == "__main__":
    b,g = map(float,input().split())
    pb = b/(b+g)
    n = 6
    c = 3
    odds = 0
    for r in range(c,n+1):
        odds += round(nCr(n,r)*((pb)**r)*((1-pb)**(n-r)),3)
    
    print(odds)

    


'''
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is . If there is  child born per birth, what proportion of Russian families with exactly  children will have at least  boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of  decimal places (i.e.,  format).

Input Format

A single line containing the following values:

1.09 1
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
'''
