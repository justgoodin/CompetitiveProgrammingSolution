
import math
if __name__ == "__main__":
    S,X,N = map(int,input().split())
    days = 0
    distance = S
    TY = []
    defDays = math.ceil(S/X)
    for i in range(N):
        TY.append(list(map(int,input().split())))

    TY.sort()
    i = 0
    while distance >0:
        if days == TY[i][0]-1:
            distance -= TY[i][1]
            days += 1
            #print(days,distance,TY[i][0])
            i += 1
        else:
            gapT = days + math.ceil(distance/X)
            if gapT > TY[i][0]:
                gapD = (TY[i][0] - TY[i-1][0])
                distance -= gapD*X
                days += gapD
            else:
                days = gapT
                distance =0
            #print(days,distance)
        
    print(days)



'''
from math import ceil
s, x, n = list(map(int, input().split()))
 
ty = []
for _ in range(n):
    ty.append(list(map(int, input().split())))
    # ty[t_i] = y_i
 
ty.sort(key=lambda x:x[0])
 
 
 
i=0
 
ty = iter(ty)
 
while s>0:
    crnt = next(ty, None)
    if crnt == None:
        i+=ceil(s/x)
        break
 
    # print(s, crnt)
    if s > (crnt[0]-(i+1))*x:
        s-=(crnt[0]-(i+1))*x
        s-= crnt[1]
        i+=((crnt[0]-(i+1))+1)
    else:
        i+=ceil(s/x)
        break
 
print(i)
'''
