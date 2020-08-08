#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mystery-30/

from sys import stdin, stdout
if __name__ == "__main__":
    for item in stdin:
        n = int(item)
        number = bin(n)
        num = str(number)
        #output = num[2:].count("1")
        print(num[2:].count("1"))