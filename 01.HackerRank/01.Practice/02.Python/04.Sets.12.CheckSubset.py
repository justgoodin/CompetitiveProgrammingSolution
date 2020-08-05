#Link to the question below
#

if __name__ == "__main__":
    T = int(input())
    A = [[]]*T
    B = [[]]*T

    for i in range(T):
        An = int(input())
        A[i] = set(map(int,input().split()))
        Bn = int(input())
        B[i] = set(map(int,input().split()))
        
        print(A[i].issubset(B[i]))