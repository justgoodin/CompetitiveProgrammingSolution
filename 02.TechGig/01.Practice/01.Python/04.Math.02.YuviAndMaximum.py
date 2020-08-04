def main():
    inputList = sorted(list(map(int,input().strip().split(" "))),reverse=True)
    print(inputList[0]+inputList[1])

main()

'''
YUVI and MAXIMUM (100 Marks)
YUVI has provided you the score of his last 6 innings and you have to tell him the maximum total of 2 innings.

Input Format
The only line of input consist of score in last 6 innings.

Constraints
1<= score <=100

Output Format
Print Maximum total of 2 innings

Sample TestCase 1
Input
1 3 7 20 29 
Output
49

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''