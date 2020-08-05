#Link to the question below
#

if __name__ == '__main__':
    n = int(input())
    
    marks =[]

    for i in range(n):
        name = input()
        score = float(input())
        marks.append([name,score])

    marks.sort(key= lambda x: x[1])
    
    a = [i for i in marks if i[1]!=marks[0][1]]
    b = [j for j in a if j[1]==a[0][1]]
    
    b.sort()

    for i in range(0,len(b)):
        print(b[i][0])