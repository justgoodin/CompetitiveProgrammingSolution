def fib(count):
    dp = []*(count+1)
    dp.append(0)
    dp.append(1)
    
    for i in range(2,count):
        dp.append(dp[i-1] + dp[i-2])

    return dp


def main():

    count = int(input())
    output = fib(count)

    for i in range(0,count):
        print(output[i],end="")
        if i<count-1:
            print(end=" ")     

main()

'''
Play with Fibonacci sequence (100 Marks)
You just need to take a number as input from stdin which will tell how many terms of the Fibonacci needs to be printed.

Input Format
You will be taking a number as an input from stdin.

Constraints
1 <= N <= 10000

Output Format
You need to print the Fibonacci series separated by space to the stdout.

Sample TestCase 1
Input
10
Output
0 1 1 2 3 5 8 13 21 34
Explanation
The twist in the Fibonacci is that it will get its next number by adding two previous numbers.

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3
'''