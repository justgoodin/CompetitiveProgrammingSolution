#Link to the question below
#

def main():

    inputString1 = input()
    inputString2 = input()
    inputString3 = "".join([inputString1.strip(),inputString2.strip()])

    print(inputString3,end="")

main()