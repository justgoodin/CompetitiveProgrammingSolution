#Link to the question below
#https://www.techgig.com/practice/question/validate-phone-numbers/ekNTZHlQd0RxR1gvUVVzcUNZdE5GUlMwV28wVS8zQVZobEdzbkdzaDlBSzBIeTFpTi9Oa3BsNVVzZUNJNm1HVw==/1

def main():
    output = "Invalid"
    valid = ["8","9"]
    num = input()
    if num[0] in valid:
        output = "YES"
    else:
        output = "NO"

    print(output)

main()