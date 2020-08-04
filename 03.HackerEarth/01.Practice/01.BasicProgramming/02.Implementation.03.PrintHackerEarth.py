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

'''
As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please help them.

Input:
The first line will consists of one integer N denoting the length of string.
Next line will contain the string  containing only lower case characters.

Output:
Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).

Constraints:

Each character of string  will be in range 
SAMPLE INPUT 
13
aahkcreeatrha
SAMPLE OUTPUT 
1
'''
