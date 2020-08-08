#Link to the question below
#https://www.techgig.com/practice/question/raghav-ceil/MXVBbG9Cam11cW0yRkw0RXplVVVqU2VQQXZxM05HLzRBeWVlU3RDZUR0Z0NYczlYNmJFNTNrR0xLeFBqNlphTw==/1


import numpy as np

def main():
    array = list(map(float,input().split()))
    npArr = np.array(array)


    A = np.ceil(npArr)

    print(A)

main()

#However, TechGig output is incorrect and they haven't bothered correcting items
#Here's a code that will work
#----------------------------------
#import math
#a=[(x) for x in input().split()]
#b=[]
#d=''
#for i in a:
#    c=str(math.ceil(float(i))) 
#    b.append((c))
#d='.  '.join(b)
#e='['+' '+d+'.'+']'
#print(e)

