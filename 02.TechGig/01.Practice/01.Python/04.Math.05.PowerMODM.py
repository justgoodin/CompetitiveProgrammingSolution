def main():

    inputList = list(map(int,input().strip().split()))
    output = inputList[0]**inputList[1]%inputList[2]

    print(output)

main()

'''
Power MOD M (100 Marks)
Ramu has a number M. Rahul provides him x and y. Rahul asks Ramu if he can find Mod M of x to power y.

Input Format
The only line of input consist of x, y and M space separately.

Constraints
1<= x, y<=10
2<= M <=10

Output Format
Print x^y mod M

Sample TestCase 1
Input
2 5 3
Output
2

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''