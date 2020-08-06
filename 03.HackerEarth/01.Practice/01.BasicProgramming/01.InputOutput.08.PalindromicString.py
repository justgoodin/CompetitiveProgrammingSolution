#Link to the question below
#

if __name__ == "__main__":
    string = input()
    size = len(string)
    mid = int(size/2)-1
    L = string[:mid]
    U = str(string[size-mid:])[::-1]

    print("YES") if L==U else print("NO")