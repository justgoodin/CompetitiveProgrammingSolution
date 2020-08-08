#Link to the question below
#

if __name__ == "__main__":
    T = int(input())
    array = list(map(int,input().split()))
    ans = 1
    for i in array:
        ans = (ans*i)%(10**9+7)

    print(ans)