#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/

if __name__ == "__main__":
    D = int(input())
    Oc,Of,Od = map(int,input().split())
    Cs,Cb,Cm,Cd = map(int,input().split())

    O = Oc+(D-Of)*Od if Of<D else Oc
    C = Cb + D/Cs*Cm + D*Cd

    if O<=C:
        print("Online Taxi")
    else:
        print("Classic Taxi")

