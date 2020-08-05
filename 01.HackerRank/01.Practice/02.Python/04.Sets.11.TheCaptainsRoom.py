#Link to the question below
#

def main(): 
    K = int(input())
    manifest = list(map(int,input().split()))

    captain = int((sum(set(manifest))*K - sum(manifest))/(K-1))

    print(captain)

main()