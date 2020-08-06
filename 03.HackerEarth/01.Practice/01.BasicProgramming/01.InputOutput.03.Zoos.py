#Link to the question below
#

if __name__ == "__main__":
    word = input()

    zCount = word.count("z")
    oCount = word.count("o")

    if zCount*2 == oCount:
        print("Yes")
    else:
        print("No")