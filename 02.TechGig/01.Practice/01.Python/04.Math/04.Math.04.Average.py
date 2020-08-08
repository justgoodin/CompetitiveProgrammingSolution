#Link to the question below
#

def main():
    count = int(input())
    power = []*count
    power = list(map(int,input().strip().split(" ")))
    average = math.fsum(power)/count

    print("{:.2f}".format(average))

main()