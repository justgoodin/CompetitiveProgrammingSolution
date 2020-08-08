#Link to the question below
#

import math

def main():

    AB = int(input())
    BC = int(input())

    CA = (AB**2+BC**2)**(1/2)
    AD = CA/2

    aBCA =  round(math.degrees(math.asin(BC/CA)))

    print(aBCA,end="")

main()