#Link to the question below
#

if __name__ == "__main__":
    N = int(input())
    string = input()
    
    hack = [["h","a","c","k","e","r","t"],[0.5,0.5,1,1,0.5,0.5,1],[0,0,0,0,0,0,0]]
    
    for i in string:
        if i in hack[0]:
            pos = hack[0].index(i)
            hack[2][pos] += hack[1][pos]

    #for i in hack[0]:
    #    print(i,":",string.count(i))
    #print(hack)
    print(int(min(hack[2])))