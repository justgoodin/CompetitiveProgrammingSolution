#Link to the question below
#

def main():
    inputString = input()
    inputRange = [int(input()),int(input())]

    print(inputString[inputRange[0]:inputRange[1]+1],end="")

main()