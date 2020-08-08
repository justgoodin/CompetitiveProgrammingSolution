#Link to the question below
#https://www.techgig.com/practice/question/max-of-min/RjdQL2ZPRTRFdURHN1I0YjJ6Z1FhN0kvVGt1R2FaanlZVmJoYmE0V3hrWTgzUjhmWnkwSTI2QkZYaU9lWXV4Zw==/1

import numpy as np
def main():
    N,M = map(int,input().split())
    A = []

    for i in range(N):
        A.append(list(map(int,input().split())))
    
    array = np.array(A)
    mini = [np.min(array[...,i]) for i in range(M)]
    print(np.max(mini),end="")
main()