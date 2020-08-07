#Link to the question below
#https://www.techgig.com/practice/question/validate-debit-card/WHdlMzVHdzRZcHVVMVVWMU8xa1VhemRmVmVuRE5ZbGtDbnpRcFpRa1N4RHNPQ2lTTTArdkpham14Y3poZVE1Zg==/1

import re
def main():
    N = int(input())
    output = "Invalid"
    for i in range(N):
        card = input()
        pattern = re.match("7|8|9d{3}-?d{4}-?d{4}-?d{4}",card)
        
        if pattern:
            output = "Valid"

        if i <N-1:
            print(output)
        else:
             print(output,end="")

main()