#Link to the question below
#https://www.techgig.com/practice/question/validate-email-address/ekJTeWFra1BqVy9NNGxXNTVMR3F5RUpla1Q2bGdXa3ZyUEViQlNKQ2hzZzRmT1lCTlZjZmF6eVZGNEt6VnVtTw==/1

#Another buggy Question that doesn't provide right answer
import re

def main():
    N = int(input())
    output = []
    for i in range(N):
        email = input()

        pattern = re.match(r"^[aA-zZ].*@...*\..*",email)
        
        if pattern:
            output.append(email)

    l = len(output)
    for i in range(l):
        if i<l-1:
            print(output[i])
        else:
            print(output[i],end="")

main()