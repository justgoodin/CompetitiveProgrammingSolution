#Link to the question below
#

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        a,b = map(int,input().split())

        radius = min(a,b)
        count = int(max([a/radius,b/radius]))

        print(count)