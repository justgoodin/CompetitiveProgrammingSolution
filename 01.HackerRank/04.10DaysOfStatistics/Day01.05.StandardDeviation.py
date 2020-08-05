#Link to the question below
#

def sigma(array,N):
    
    m = sum(array)/N
    distance = 0

    for x in array:
        distance += (x-m)**2

    output = round((distance/N)**(1/2),1)

    return output


def main():
    N = int(input())
    array = list(map(int,input().split()))

    print(sigma(array,N))

main()