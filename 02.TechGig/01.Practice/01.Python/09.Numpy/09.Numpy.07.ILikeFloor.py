#Link to the question below
#https://www.techgig.com/practice/question/i-like-floor/UDZub1ZiQjNGbG9SdFlHbzVSVndudWxBc2V4Vk5IaVFncnlUbXcwc3hndGhUR0dlZkx5MWhzQXl6c3BUNTBzUw==/1


import numpy as np

def main():
    array = list(map(float,input().split()))
    npArr = np.array(array)


    A = np.floor(npArr)

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
#    c=str(math.floor(float(i))) 
#    b.append((c))
#d='.  '.join(b)
#e='['+' '+d+'.'+']'
#print(e)

