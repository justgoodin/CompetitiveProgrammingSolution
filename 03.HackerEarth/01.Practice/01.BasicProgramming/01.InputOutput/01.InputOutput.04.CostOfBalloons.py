#Link to the question below
#

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        green,purple = map(int,input().split())
        participants = int(input())
        solution = [[]]*participants

        for i in range(participants):
            solution[i] = list(map(int,input().split()))
            
        sum1 = sum(row[0] for row in solution)
        sum2 = sum(row[1] for row in solution)
        output = min(sum1*green+sum2*purple,sum1*purple+sum2*green)
        print(output)