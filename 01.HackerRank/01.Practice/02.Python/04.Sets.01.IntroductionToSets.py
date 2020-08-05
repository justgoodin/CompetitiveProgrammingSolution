#Link to the question below
#

def average(array):
    setArray = set(array)
    result = sum(setArray)/len(setArray)

    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)