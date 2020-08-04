def main():
    
    count = int(input())
    inputList = list(map(int,input().split(" ")))
    
    inputTuple = tuple(inputList)

    print(hash(inputTuple))

main()

'''
Tuple and Hash (100 Marks)
There are N number of integers. You have to create a tuple of N integers and compute the hash of the tuple.

Input Format
The first line of input consist of number of integers, N
The second line of input consist of N space separated integers.

Constraints
1<= N <=10
1<= Ai <= 10

Output Format
Print the hash of the tuple

Sample TestCase 1
Input
2
2 3
Output
3713082714463740756

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''

