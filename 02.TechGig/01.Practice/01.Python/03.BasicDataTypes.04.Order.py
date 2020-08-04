def main():

    count = int(input())
    inputList = []

    for i in range(0,count):
        inputList.append((input()))

    sortedList = sorted(inputList)

    for i in range(0, count):
        print(sortedList[i])

main()


'''
Order (100 Marks)
There are N members of a committee. A list is to made in alphabetical order.

Input Format
The first line of input consist of number of members, N.
Next N lines consist of name of members.

Constraints
1<= N <=10

Output Format
Print the name in alphabetical order.

Sample TestCase 1
Input
5
Rahul
Alia
Sushma
Faruk
Varun

Output
Alia
Faruk
Rahul
Sushma
Varun

Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''
