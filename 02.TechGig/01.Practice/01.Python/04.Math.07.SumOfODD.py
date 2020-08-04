def main():

    count = int(input())
    inputList = list(map(int,input().strip().split()))
    sum =0

    for i in range(0,count):
        if inputList[i]%2 == 0:
            sum += inputList[i]

    print(sum)

main()

'''
Sum of ODDs (100 Marks)
Given N integers, find the sum of all the oddly placed integers. 

Input Format
The first line of input consist of number of integers, N
The second line of input consist of N space separated integers.

Constraints
1<= N <=10
1<= Ai <=100

Output Format
Print the sum of oddly placed integers.

Sample TestCase 1
Input
5
1 2 3 4 5 
Output
6

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''
