#Link to the question below
#https://www.techgig.com/practice/question/shape-and-reshape/OW4rNEpJWFEvNlZrQ0VVdEI2VTQ4QjhEbE9wOGh2SG00RFE1ODgvVzlWazI1Rk5jdjlSK0tQZHI4WVVFdzBLSw==/1

import numpy as np
def main():

    array = list(map(int,input().split()))
    npArray  = np.array(array)

    output = npArray.reshape(3,3)
    print(output,end="")

main()