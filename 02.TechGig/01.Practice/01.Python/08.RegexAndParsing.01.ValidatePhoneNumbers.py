#Link to the question below
#https://www.techgig.com/practice/question/validate-phone-numbers/ekNTZHlQd0RxR1gvUVVzcUNZdE5GUlMwV28wVS8zQVZobEdzbkdzaDlBSzBIeTFpTi9Oa3BsNVVzZUNJNm1HVw==/1

def main():
    N = int(input())
    output = "Invalid"
    valid = ["1","2"]
    for i in range(N):
        num = input()
        if num[0] in valid and len(num)==13:
            output = "Valid"
        else:
            output = "Invalid"

        if i <N-1:
            print(output)
        else:
            print(output,end="")

main()