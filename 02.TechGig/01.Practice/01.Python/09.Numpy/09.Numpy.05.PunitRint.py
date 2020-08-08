#Link to the question below
#https://www.techgig.com/practice/question/punit-rint/WVEzWndKWGtCams1VU41a3VaVC9xaTFFSkNlMkErVER1QUkwUUhZY0RCKytYRTIxaC9NS3NFdGt6QlJqbXJ4eQ==/1

import numpy as np

def main():
    array = list(map(float,input().split()))
    npArr = np.array(array)


    A = np.rint(npArr)

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
#    if i[2]>='5':
#         c=str(math.ceil(float(i))) 
#         b.append((c))
#    else: 
#        c=str(math.floor(float(i))) 
#        b.append((c))
#d='.  '.join(b)
#e='['+' '+d+'.'+']'
#print(e)