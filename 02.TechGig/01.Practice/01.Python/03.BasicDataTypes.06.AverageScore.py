def main():

    count = int(input())
    inputList = [[]*4]*count
    sum = 0
    for i in range(0,count):
        inputList[i]=list(map(str,input().split(" ")))

    playerList = []
    
    for i in range(0,count):
        playerList.append(inputList[i][0])
     
    player = input()
    
    for  i in range(1,4):
        sum += int(inputList[playerList.index(player)][i])

    print('{:.2f}'.format(float(sum/3)))

main()

'''
Average Score (100 Marks)
There are N players with their score in last 3 matches. You will have to create a dictionary and output the average score of the player asked upto 2 decimal places.

Input Format
The first line of input consist of number of players, N
Next N lines consists of player name and their score in last three matches space separately.
The last line of the input consist of the player in question.

Constraints
1<= N <=10

Output Format
Print the average score of the player asked.

Sample TestCase 1
Input
3
Warner 150 100 120
Kohli 10 30 20
Rohit 60 80 40
Kohli

Output
20.00

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''
