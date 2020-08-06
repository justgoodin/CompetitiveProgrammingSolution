def main():

    inputString = input()
    char = input()
  
    try:
        position = inputString.index(char)
        print("True",end="")
    except:
        print("False",end="")

main()