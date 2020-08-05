#Link to the question below
#

if __name__ == "__main__":
    A = set(map(int,input().split()))
    n = int(input())

    B = [[]]*n
    flag = True
    for i in range(n):
        B[i] = set(map(int,input().split()))
        flag = A > B[i]
        if flag == False:
            break
    
    print(flag)