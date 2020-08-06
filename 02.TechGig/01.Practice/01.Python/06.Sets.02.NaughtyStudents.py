#Link to the question below
#https://www.techgig.com/practice/question/naughty-students/U3VGTEtKRkFHdUVadWpDVVV3OVNIcDFNMjUxcVBiYVdLNHNjQ2NFNUdLU3FucEUxMDlHczJpOHNqNDh3NU9MWg==/1

def main():
    An = int(input())
    A = set(map(int,input().strip().split()))
    Bn = int(input())
    B = set(map(int,input().strip().split()))

    count = len(A.symmetric_difference(B))
    if count==3:
        print(count,end="")
    else:
        print(count)

main()