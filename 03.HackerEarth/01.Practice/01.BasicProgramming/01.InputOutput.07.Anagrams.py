#Link to the question below
#

import math 

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        string1 = list(input())
        string2 = list(input())
        total = string1+string2
        word1 = set(string1)
        word2 = set(string2)
        count=0
        
        for j in set(total):
            count += abs(string1.count(j)-string2.count(j))
            
        print(count)