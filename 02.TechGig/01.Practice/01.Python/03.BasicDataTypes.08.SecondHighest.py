def main():

    count = int(input())

    names = []
    marks = []
    finalList = []
    for i in range(0,count):
        names.append(input())
        marks.append(int(input()))

        sortedMarks = sorted(marks,reverse=True)
        second = 0
    for i in range(1,count):
        second = sortedMarks[1]
        if second > sortedMarks[i]:
            continue
        else: 
            break
        
    for i in range(count):
        if marks[i]==second:
            finalList.append(names[i].strip())

    sortedList = sorted(finalList)

    for i in range(len(sortedList)):
        print(sortedList[i],end="")
        if i < len(sortedList)-1:
            print()

main()

'''
Second Highest (100 Marks)
There are a total N students present in today's class. You are given student names and their respective height (in cms).
You have to find names of all the second highest students (according to their heights).
If there are multiple students , print each name on new line.

Input Format
First line will contain an Integer N, denoting the number of students.
Next 2 * N lines contains description of each student. first line contains name of the student and second line contains height of the student.

Constraints
1 <= N <= 100

Output Format
Print name of all the students having second highest height in alphabetical order.

Sample TestCase 1
Input
4
saurabh 
102
arpit
120
aditya
102
varun
101

Output
aditya
saurabh

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
Python, Python 3, Pypy
'''