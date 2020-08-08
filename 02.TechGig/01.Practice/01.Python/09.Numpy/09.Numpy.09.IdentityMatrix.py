#Link to the question below
#https://www.techgig.com/practice/question/identity-matrix/a2I4ZGIzN1lFZ2JCaDlnSzVRN1ppWFNhTHNwMm0yZnRFVUJ6bnN2bTA4QVVvck44aGRUSGlXdUMrcWRvbXdJTA==/1

import numpy as np

def main():
    N = int(input())
    A = []

    for i in range(N):
        B = []
        for j in range(N):
            if i==j:
                B.append(1)
            else:
                B.append(0)
        A.append(B)

    print(np.array(A),end="")

main()