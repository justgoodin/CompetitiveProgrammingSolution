def main():
    count = int(input())
    power = []*count
    power = list(map(int,input().strip().split(" ")))
    average = math.fsum(power)/count

    print("{:.2f}".format(average))

main()
'''
Average (100 Marks)
The power of N villains is provided to you. You have to find the average power of all villains upto 2 decimal places.

Input Format
The first line of input consist of number of villains, N
The second of input consist of power of N villains space separated.

Constraints
1<= N <=10
1<= Power <=100

Output Format
Print the average power upto 2 decimal places.

Sample TestCase 1
Input
4
3 4 5 4 
Output
4.00

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''