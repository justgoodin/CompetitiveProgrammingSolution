#Link to the question below
#

def swap_case(s):
    newString = s.swapcase()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)