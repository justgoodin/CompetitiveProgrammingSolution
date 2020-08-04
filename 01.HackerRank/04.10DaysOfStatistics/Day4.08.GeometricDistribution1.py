if __name__ == "__main__":
    numerator, denominator = map(int,input().split())
    n = int(input())

    p = numerator/denominator
    output = (1-p)**(n-1)*p
    print(round(output,3))


    
'''
Objective
In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning materials!

Task
The probability that a machine produces a defective product is . What is the probability that the  defect is found during the  inspection?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:

1 3
5
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
'''
