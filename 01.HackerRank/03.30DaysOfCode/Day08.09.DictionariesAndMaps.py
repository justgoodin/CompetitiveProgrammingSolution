#Link to the question below
#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true

import sys

if __name__ == "__main__":
    n = int(input())
    directory = {}

    for i in range(n):
        name, num = map(str,input().split())
        directory[name]=num

    #print(directory)

    for name in sys.stdin:
        try:
            name = name.strip() #Removing newlines WTF
            print(name+"="+directory[name])
        except KeyError:
            print("Not found")