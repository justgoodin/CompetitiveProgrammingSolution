#Link to the question below
#

if __name__ == "__main__":
    X,K = map(str,input().split())
    K = int(K)
    output = str()
    for i in X:
        
        if i!="9" and K > 0:
            output += "9"
            K -= 1
        else:
            output += i

    print(output)