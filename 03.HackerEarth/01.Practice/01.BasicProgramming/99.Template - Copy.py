#Solution Here

import math
if __name__ == "__main__":
    S,X,N = map(int,input().split())
    days = 0
    distance = S
    TY = []
    #print("here")
    defDays = math.ceil(S/X)
    for i in range(N):
        TY.append(list(map(int,input().split())))
    
    TY.sort()
    print(TY)
    i = 0
    pas = 0
    while distance > 0:
        pas += 1
        #print("TY",TY[i][0],TY[i][1])
        try:
            if TY[i][0]-1 == days:
                distance -= TY[i][1]
                days += 1
                i += 1
                #print(1,pas,i,days,distance)
            else:
                Ti = TY[i][0]
                Tj = TY[i-1][0]+1 if i>0 else 1
                yGap = (Ti - Tj)*X
                if yGap<distance:
                    distance -= yGap
                    days += yGap//X
                    #print(2,pas,i,days,distance)
        except:
            #print("here")
            days += math.ceil(distance/X)
            distance -= X*math.ceil(distance/X)
            #print(3,pas,i,days,distance)
    
    print(days)
            



'''
#Link to Question Here

#Question Below for reference
'''
