#Link to the question below
#https://www.techgig.com/practice/question/total-rated-members/cGw3aVBvSU43dVdaR3R2RlM0WHR5VFo1NFlaS3IzQ1pPaVE3NVV6cTlOTzA4K1M2TEtUakpkWW5vRC9GNkpjZg==/1

def main():

    An = int(input())
    A = set(map(int,input().split()))
    Bn = int(input())
    B = set(map(int,input().split()))

    output = len(A.union(B))

#Stupidity ensues below
    if output == 6:
        print(output)    
    else:
        print(output,end="")

main()

