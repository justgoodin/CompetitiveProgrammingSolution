#Link to the question below
#https://www.techgig.com/practice/question/validate-debit-card/WHdlMzVHdzRZcHVVMVVWMU8xa1VhemRmVmVuRE5ZbGtDbnpRcFpRa1N4RHNPQ2lTTTArdkpham14Y3poZVE1Zg==/1

import re

def main():
    N = int(input())

    for i in range(N):
        card = re.sub(r"\D","",input())
        output = "Invalid"
        pattern = re.match(r"^[7-9][0-9]{15}$",card)

        if pattern:
            output = "Valid"

        if i <N-1:
            print(output)
        else:
            print(output,end="")
        

main()