#Link to the question below
#

if __name__ == "__main__":
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    
    for i in range(Q):
        Q = list(map(int,input().split()))
        if Q[0] == 1:
            A[Q[1]] = Q[2]
        elif Q[0] == 2:
            try:
                print(sum(A[Q[1]:Q[2]+1]))
            except:
                print(-1)