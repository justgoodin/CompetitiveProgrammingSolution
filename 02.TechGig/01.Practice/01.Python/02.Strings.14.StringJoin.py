#Link to the question below
#

def main():

    separator = input()
    inputString = []
    
    while(True):
        try:
            ch=input()
        except:
            break;
        inputString.append(ch)

    outputString = separator.join(inputString)
    print(outputString,end="")

main()