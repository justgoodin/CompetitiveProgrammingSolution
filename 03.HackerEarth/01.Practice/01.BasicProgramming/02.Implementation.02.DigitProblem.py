if __name__ == "__main__":
    X,K = map(str,input().split())
    K = int(K)
    output = str()
    for i in X:
        
        if i!="9" and K > 0:
            output += "9"
            K -= 1
        else:
            output += i

    print(output)

'''
This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:

First line of the input contains two integers X and K separated by a single space.

Output:

Print the largest number formed in a single line.

Constraints:


SAMPLE INPUT 
4483 2
SAMPLE OUTPUT 
9983
'''
