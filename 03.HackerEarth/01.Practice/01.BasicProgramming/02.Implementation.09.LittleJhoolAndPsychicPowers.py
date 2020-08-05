#Link to the question below
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/

if __name__ == "__main__":
    string = input()
    n = len(string)
    output = "Good luck!"
    for i in range(n-6):
        sub = string[i:i+6]

        if sub == "000000" or sub == "111111":
            output = "Sorry, sorry!"
            break
    
    print(output)



