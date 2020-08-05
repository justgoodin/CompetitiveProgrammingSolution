#Link to the question below
#

def print_formatted(number):
    for i in range(1,number+1):
        size = len('{0:b}'.format(number))
        print('{0:d}'.format(i).rjust(size),end="")
        print('{0:o}'.format(i).rjust(size+1),end="")
        print('{0:X}'.format(i).rjust(size+1),end="")
        print('{0:b}'.format(i).rjust(size+1))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)