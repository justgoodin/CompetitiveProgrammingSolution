#Link to the question below
#https://www.techgig.com/practice/question/determinant-of-a-matrix/V2ozTDVFU3o5TUpYejc5elRzeDYwcWdKbHA0Y1ByMnNyYUJwQ3pwYjd4ajgyZEhUcDM5YnBQVGtDeWl0eUVyNA==/1

import numpy as np

def main():
    N = int(input())
    A = [[]*N]*N

    for i in range(N):
        A[i] = list(map(int,input().split()))

    #array = np.array(A)

    print(np.linalg.det(A),end="")

main()


