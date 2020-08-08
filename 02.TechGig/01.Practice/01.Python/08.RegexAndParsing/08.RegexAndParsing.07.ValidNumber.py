#Link to the question below
#https://www.techgig.com/practice/question/valid-number/Q0t1NVhmQzdROW1lU1FMTVc5dVJrZnN6UXdRV2pvbXQ4ekVaMDlvNmtmNTRnbHpiVWRrV3MzaC9ScTc0RE9nRQ==/1

def main():
    number = input()
    valid = ["3","5","7"]

    output = str()

    if number[0] in valid:
        output = "TRUE"
    else:
        output = "FALSE"

    print(output)

main()