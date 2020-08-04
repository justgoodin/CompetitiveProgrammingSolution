#Link to the question below
#https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

T = int(input())

for i in range(T):
    string = input()
    odd = string[1::2] #string[starting index: ending index -1: steps]
    even = string[0::2]
    print(even+" "+odd)