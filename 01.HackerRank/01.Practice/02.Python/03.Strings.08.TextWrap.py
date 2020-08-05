#Link to the question below
#

import textwrap
def wrap(string, max_width):
    
    newString = textwrap.fill(string,width=max_width)
    return newString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)