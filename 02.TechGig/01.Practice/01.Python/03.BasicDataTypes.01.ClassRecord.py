#Link to the question below
#

def main():
    
    count = int(input())
    record = [[]*5]*count
    
    for i in range(0,count):
        record[i] = list(map(str,input().split(" ")))
    
    for i in range(1,6):
        sumOfMarks=0
        for j in range(0,count):
            sumOfMarks=sumOfMarks+float(record[j][i])
        print("{:.2f}".format(sumOfMarks/count),end="")
        if i<5:
            print(end=" ")

main()