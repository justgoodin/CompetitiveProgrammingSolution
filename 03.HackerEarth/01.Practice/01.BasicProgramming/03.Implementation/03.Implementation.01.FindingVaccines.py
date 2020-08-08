#Link to the question below
#

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    r = input()
    
    gV,cV = [r.count("G"),r.count("C")]
    best = 0
    index = 0
    
    for i in range(n):
    
        l = int(input()) #useless input
        string = (input()) 
        
        G = string.count("G")
        C = string.count("C")
        interaction = G*cV + C*gV
        
        if interaction>best:
            best = interaction
            index = i+1
    
    print(index)