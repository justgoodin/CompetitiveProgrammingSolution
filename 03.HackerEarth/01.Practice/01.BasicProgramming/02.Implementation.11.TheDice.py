#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-dice-d4dc5b11/

if __name__ == "__main__":
    rolls = input()
    check = "6"
    count = 0

    if rolls[-1]!=check:
        for item in rolls:
            if item == check:
                continue
            else:
                count += 1
    else:
        count = -1

    print(count)

