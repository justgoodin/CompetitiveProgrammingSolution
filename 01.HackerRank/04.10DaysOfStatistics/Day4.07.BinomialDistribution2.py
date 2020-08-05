#Link to the question below
#

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