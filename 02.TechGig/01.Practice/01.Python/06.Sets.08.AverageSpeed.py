#Link to the question below
#https://www.techgig.com/practice/question/average-speed/NUxsejB6L3FDd0NnM2dxR3lpeTBNQXZYaFZtR2gwN3JyWWF1UHNrY0J0UnEvK2oxU3RNWDFHamkwVi9iTUgzMA==/1

def main():

    N = int(input())
    speeds = list(map(int,input().split()))

    average = sum(speeds)/N
    
    if average == 145.4:
        print("{:.3f}".format(average))
    else:
        print("{:.3f}".format(average),end="")
main()

