#Link to the question below
#

import cmath
if __name__ == "__main__":
    p = complex(input())

    r = abs(p)
    d = cmath.phase(p)
    print(r)
    print(d)