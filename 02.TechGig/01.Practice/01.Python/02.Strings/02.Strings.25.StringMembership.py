#Link to the question below
#

def main():

    inputString = input()
    char = input()

    try:
        inputString.index(char)
        print("True",end="")
    except:
        print("False",end="")

main()