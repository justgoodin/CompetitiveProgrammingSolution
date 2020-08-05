#Link to the question below
#

import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())

    CA = (AB**2 + BC**2)**(1/2)

    DB = CA/2 #D being the mid point and not M, idiots

    #DB:DC::<DBC:<BCD
    #DB = DC, hence <DBC = <BCD 

    BCA = round(math.degrees(math.acos(BC/CA)))
	#Even better solution that doesn't require computing CA below
	#BCA = round(math.degrees(math.atan2(AB,BD)))
    print(str(BCA)+"°")