#Link to the question below
#

if __name__ == "__main__":
    L = int(input())
    N = int(input())

    for i in range(N):
        W,H = map(int,input().split())

        if W >= L and H >= L:
            print("ACCEPTED") if W==H else print("CROP IT")
        else:
            print("UPLOAD ANOTHER")