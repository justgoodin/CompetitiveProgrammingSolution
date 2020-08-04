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


'''
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like


So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS
1<=T<=105
1<=N<=108
SAMPLE INPUT 
2
18
40
SAMPLE OUTPUT 
19 WS
45 AS
'''
