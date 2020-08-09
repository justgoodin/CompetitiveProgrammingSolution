#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/hawkeye-and-floodfill/

def painter(y,x,i,j,p):
    dy = p - abs(i-y)
    dx = p - abs(j-x)

    return min(max(dy,0),max(dx,0))


if __name__ == "__main__":
    N = int(input())
    i,j,p = map(int,input().split())
    
    for y in range(N):
        for x in range(N):
            print(painter(y,x,i,j,p),end="")
            if x <N-1:
                print(end=" ")
        print()