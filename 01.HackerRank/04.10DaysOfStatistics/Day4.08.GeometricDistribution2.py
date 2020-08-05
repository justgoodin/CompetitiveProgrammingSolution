#Link to the question below
#

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