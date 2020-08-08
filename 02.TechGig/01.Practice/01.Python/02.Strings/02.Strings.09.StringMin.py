#Link to the question below
#

def main():

    x = input()
    y=min(x.lower().replace(" ",""))
    z =min(x.replace(" ",""))

    if y<z.lower():
        print(y,end="")
    else:
        print(z,end="")

main()