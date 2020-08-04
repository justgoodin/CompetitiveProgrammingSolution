def main():

    count = int(input())
    marksList = sorted(list(map(int,(input().strip().split(" ")))),reverse=True)
    secLowest = marksList[0]

    for i in range(1,count):
        secLowest = marksList[i]
        if secLowest ==marksList[i-1]:
            continue
        else:
            break

    print(secLowest)    

main()

'''
Second Maximum (100 Marks)
The marks of Ranu are given in N subjects and you have to tell him the second maximum marks he has got.
Marks may or may not duplicate.

Input Format
The first line of input consist of number of subjects, N.
The second line of input consist of N separated marks. 

Constraints
1<= N <=10
1<= Ai <=100

Output Format
Print the second maximum marks Ranu has got.

Sample TestCase 1
Input
5
3 9 9 5 4 
Output
5

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''
