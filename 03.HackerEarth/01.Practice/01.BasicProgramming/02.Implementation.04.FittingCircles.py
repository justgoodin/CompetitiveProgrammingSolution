if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        a,b = map(int,input().split())

        radius = min(a,b)
        count = int(max([a/radius,b/radius]))

        print(count)



'''
You are given a rectangle of length  and width . You are required to determine a circle that contains the maximum circumference that fits inside the rectangle. This type of circle is called a big circle. Your task is to determine the maximum number of big circles that can fit inside the rectangle. 

Input format

First line: An integer  denoting the number of test cases
First line of each test case: Integers  and 
Output format

For each test case, print the answer on a new line denoting the maximum number of big circles that can fit in the provided rectangle.  

Constraints


SAMPLE INPUT 
1
40 10
SAMPLE OUTPUT 
4
'''
