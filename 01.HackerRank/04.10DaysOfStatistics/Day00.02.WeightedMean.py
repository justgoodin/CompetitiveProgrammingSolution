#Link to the question below
#

def mean(array):

    output = sum([i*j for i,j in zip(array[0],array[1])])/sum(array[1])
    output = round(output,1)
    return output

def main():
    N = int(input())
    elements =[[0]*5]*2

    elements[0] = list(map(int,input().strip().split()))
    elements[1] = list(map(int,input().strip().split()))


    print(mean(elements))

main()