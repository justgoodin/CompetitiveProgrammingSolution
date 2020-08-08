#Link to the question below
#

if __name__ == "__main__":
    l,r,k = map(int,input().split())
    count = len([i for i in range(l,r+1) if i%k==0])

    print(count)