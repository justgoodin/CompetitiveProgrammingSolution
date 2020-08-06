#Link to the question below
#

def seatType(seat):
    WS = [1,6,7,0]
    MS = [2,5,8,11]
    AS = [3,4,9,10]
    if seat%12 in WS:
        output = "WS"
    elif seat%12 in MS:
        output = "MS"
    else: 
        output = "AS"
    return output

def oppSeat(seat):
    index = seat%12
    if index==0: 
        index=12
    output = seat + (11-2*(index-1))
    return output


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        seatNo = int(input())
        opp = oppSeat(seatNo)
        print(opp,seatType(opp))