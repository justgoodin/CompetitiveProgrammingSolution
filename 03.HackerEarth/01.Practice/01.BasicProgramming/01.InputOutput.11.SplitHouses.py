#Link to the question below
#

if __name__ == "__main__":
    n = int(input())
    space = input()

    count = 0

    print("NO") if "HH" in space else print("\n".join(["YES",space.replace(".","B")]))