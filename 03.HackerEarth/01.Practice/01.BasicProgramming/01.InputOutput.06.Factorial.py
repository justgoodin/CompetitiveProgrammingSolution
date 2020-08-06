#Link to the question below
#

def fact(n):
    output = n*fact(n-1) if n>1 else 1
    
    return output
        


if __name__ == "__main__":
    N = int(input())

    print(fact(N))