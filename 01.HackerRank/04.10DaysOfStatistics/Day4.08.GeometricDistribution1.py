#Link to the question below
#

if __name__ == "__main__":
    numerator, denominator = map(int,input().split())
    n = int(input())

    p = numerator/denominator
    output = (1-p)**(n-1)*p
    print(round(output,3))