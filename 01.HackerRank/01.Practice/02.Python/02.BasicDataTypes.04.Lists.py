#Link to the question below
#

if __name__ == '__main__':
    N = int(input())
    commands = [[]]*N

    for i in range(N):
        commands[i] = list(map(str,input().strip().split()))

    final = []

    for value in commands:
        if value[0] == "insert":
            final.insert(int(value[1]),int(value[2]))
        elif value[0] == "remove":
            final.remove(int(value[1]))
        elif value[0] == "append":
            final.append(int(value[1]))
        elif value[0] == "print":
            print(final)
        elif value[0] == "sort":
            final.sort()
        elif value[0] == "reverse":
            final.reverse()
        elif value[0] == "pop":
            final.pop()