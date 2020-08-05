#Link to the question below
#

def median(array):
    #array.sort()
    index = int(len(array)/2)
    if (len(array))%2 ==0:
        output = int((array[index-1]+array[index])/2)
        #print(index,output)
    else:
        output = array[index]

    return output

def quartile(array, Qn):
    output = [0]*3
    output[1] = median(array)
    output[0] = median([i for i in array if i<output[1]])
    output[2] = median([i for i in array if i>output[1]])

    return output[Qn-1]


def main():
    n = int(input())
    array = sorted(list(map(int,input().split())))   

    print(quartile(array,1))
    print(quartile(array,2))
    print(quartile(array,3))

main()