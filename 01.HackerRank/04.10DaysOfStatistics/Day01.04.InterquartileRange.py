#Link to the question below
#

def median(array):
    index = int(len(array)/2)
    #print(index)
    if (len(array))%2 ==0:
        output = float(array[index-1]+array[index])/2
    else:
        output = float(array[index])

    return [output,index,len(array)%2]

def interQuartile(array):
    
    Q2 = median(array)
    if len(array)%2==0:
        L = array[:Q2[1]]
        U = array[Q2[1]:]
    else:
        L = array[:Q2[1]-1]
        U = array[Q2[1]+1:]

    Q1 = median(L)
    Q3 = median(U)
    output = Q3[0] - Q1[0]

    return output


def main():
    n = int(input())
    X = list(map(int,input().split()))
    F = list(map(int,input().split()))
    array = []

    for f,x in zip(F,X):
        for i in range(f):
            array.append(x)

    array.sort()
    print(interQuartile(array))


main()