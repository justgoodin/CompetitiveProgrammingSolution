#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/rain-41f57695/

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        l,r,s = map(int,input().split())
        #print(l/s,r/s)
        
        min = l//s + (0 if l%s==0 else 1)
        max = r//s

        if min==0 or max==0 or min>max:
            print(-1,-1)
        else:
            print(min,max)


