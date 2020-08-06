#Link to the question below
#

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