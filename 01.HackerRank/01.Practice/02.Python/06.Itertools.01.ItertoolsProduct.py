#Link to the question below
#https://www.hackerrank.com/challenges/itertools-product/problem


from itertools import product

def main():

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AxB = list(product(A,B))

    for item in AxB:
        print(item, end=" ")

main()