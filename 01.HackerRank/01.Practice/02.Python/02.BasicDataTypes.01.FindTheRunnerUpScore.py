#Link to the question below
#

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())),reverse=True)

    maxVal = max(arr)

    for value in arr:
        if value<maxVal:
            maxVal=value
            break
    print(maxVal)