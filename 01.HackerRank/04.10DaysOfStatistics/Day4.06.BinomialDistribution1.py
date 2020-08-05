#Link to the question below
#

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