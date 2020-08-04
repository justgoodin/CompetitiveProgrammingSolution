def main():
    
    count = int(input())
    record = [[]*5]*count
    
    for i in range(0,count):
        record[i] = list(map(str,input().split(" ")))
    
    for i in range(1,6):
        sum=0
        for j in range(0,count):
            sum=sum+float(record[j][i])
        print("{:.2f}".format(sum/count),end="")
        if i<5:
            print(end=" ")

main()

'''
Class Record (100 Marks)
You are given a dataset of N students belonging to the same class.
The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemsistry, Maths, English, Hindi.
Your task is find the average marks of the class for each individual subject.

Input Format
First line will contain an Integer N, denoting  the number of students in the class.
Each of the Next N lines will contain a string S denoting the student name, followed by five integers m1, m2, m3, m4, m5 denoting the marks scored in each subject.

Constraints
1 <= N <= 10^3
1 <= S <= 10^2
0 <= m1, m2, m3, m4, m5 <= 100

Output Format
You have to print average marks upto two decimal places for each subject followed by a space. 

Sample TestCase 1
Input
2
arpit 100 75 40 56 53
anushka 100 100 76 100 100
Output
100.00 87.50 58.00 78.00 76.50

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''
