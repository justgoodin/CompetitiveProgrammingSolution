#Link to the question below
#

def mutate_string(string, position, character):
    listString = list(string)
    listString[position] = character
    string = "".join(listString)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)