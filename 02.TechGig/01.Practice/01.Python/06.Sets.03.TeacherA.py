#Link to the question below
#https://www.techgig.com/practice/question/teacher-a/ZG13TkJoZUhoaThvVWZvdjJ0T25aL3RmR3JZdXJQOXNDc0RmUmIzbk1ET1FvWmQ5d2dHNDc4VFlZVmlRNEtwZg==/1


def main():

    An = int(input())
    A = set(map(int,input().split()))
    Bn = int(input())
    B = set(map(int,input().split()))

    output = len(A.difference(B))

    print(output)

main()

