#Link to the question below
#https://www.techgig.com/practice/question/validate-phone-numbers/ekNTZHlQd0RxR1gvUVVzcUNZdE5GUlMwV28wVS8zQVZobEdzbkdzaDlBSzBIeTFpTi9Oa3BsNVVzZUNJNm1HVw==/1


#Solved using RegEx
import re

def main():
    N = int(input())
    
    for i in range(N):
        output = "Invalid"
        num = input()
        pattern = re.match(r"^[1-2][0-9]{12}",num)
        
        if pattern:
            output = "Valid"

        if i <N-1:
            print(output)
        else:
            print(output,end="")

main()
