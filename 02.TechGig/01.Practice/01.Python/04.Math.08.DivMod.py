def main():
    inputList = list(map(int,input().strip().split()))

    output = divmod(inputList[0],inputList[1])
    print(output)

main()
'''
DivMod (100 Marks)
Rohan want to find the divmod of x and y Using the divmod() function. Can you help him ?

Input Format
The only line of input consist of two space separated integers, x and y.

Constraints
1<= x, y <=100

Output Format
Print the divmod of x and y

Sample TestCase 1
Input
45 4
Output
(11, 1)

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''