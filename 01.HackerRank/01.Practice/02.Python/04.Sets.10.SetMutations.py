#Link to the question below
#

if __name__ == '__main__':
    _ = int(input())
    A = set(map(int,input().strip().split()))
    N = int(input())

    for i in range(N):
        io = input().strip().split()
        B = set(map(int,input().strip().split()))
        getattr(A,io[0])(B) #getattr to fetch the method since the commands are actual methods. If they weren't, a tuple with could be used

    print(sum(A))