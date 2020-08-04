def main():

   count = int(input())
   score = []
    
   for i in range(0,count):
      score.append(int(input())) 
	  
   print(max(score))

main()

'''
Highest Score (100 Marks)
The score of N players is given and you have to find the highest score of an individual.

Input Format
The first line of input consists of number of players, N
The second line of input consist of N separated scores of players

Constraints
1<= N <=11
1<= score <=150

Output Format
Print the highest score

Sample TestCase 1
Input
5
12
14
19
67
89
Output
89


Time Limit(X):
1.00 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3
'''

