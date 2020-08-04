'''
Corona Warriors (100 Marks)
The country is fighting with the Corona pandemic and Corona Warriors are at front dealing with all issues. There are P number of patients and D number of doctors available for the treatment. PM Modi knows the fight is long so he wants to make sure the team of doctors is applying the minimum efforts. His slogan is - ”Minimum Efforts, Maximum Results”.

For smooth functioning, PM Modi has formed a task force which will make sure the minimum efforts are used. The doctors know the efforts they will have to apply to treat a patient and have shared the data with the task force. The task force will assign the patients to the doctors making sure the minimum efforts are required. There are two main conditions which will help in minimising the total efforts and should be met:

1. Doctors should treat consecutive patients. This is a request made by doctors to the task force and has to be followed.
2. The doctors should be chosen to treat patients such that the total efforts are minimum.

Example:
Number of patients, P = 4
Number of doctors, D = 2

For Doctor 1, 
Patients    P1  P2  P3  P4
Efforts     2   2   2   2

For Doctor 2,
Patients    P1  P2  P3  P4
Efforts     3   1   2   3

While making assignments, the two stated conditions should be met.
Case 1: All the patients are assigned to Doctor 1
Efforts = 2 + 2 + 2 + 2 = 8

Case 2: All the patients are assigned to Doctor 2
Efforts = 3 + 1 + 2 + 3 = 9
This case is nullified as the efforts made in Case 1 are less than the efforts made in Case 2.

Case 3: Patient P1 is assigned to Doctor 1 and patients P2, P3 and P4 are assigned to Doctor 2
Efforts = 2 + 1 + 2 + 3 = 8

Case 4: Patients P1, P2, P3 are assigned to Doctor 2 and patient P4 is assigned to Doctor 1
Efforts = 3 + 1 + 2 + 2 = 8

Case 5: Patients P1 and P2 are assigned to Doctor 2 and patients P3 and P4 are assigned to Doctor 1
Efforts = 3 + 1 + 2 + 2 = 8 

Any other assignments of patients to Doctors will either result in more efforts required or violation of the Conditions.
Thus, the minimum efforts required to treat all patients = 8.

The task force has assigned the patients to doctors and have calculated the efforts required. They want to cross-check if the efforts they have calculated are minimum or they need to make changes into their assignment. Can you provide the minimum efforts required so that they can validate the assignment?

Input Format
The first line of input consists of two space-separated integers, number of patients, P, and number of Doctors, D.

Next D lines each consists of P space-separated efforts required by the doctor. Di line represents the efforts required by the ith doctor to treat P patients respectively.

Constraints
1<= D <=10
0<= Efforts <=1000
1<= P <=20

Output Format
Print the minimum efforts required to treat the P patients.  Note: There is a new line at the end of the output.

Sample TestCase 1
Input
4 2
2 2 2 2
3 1 2 3
Output
8
Explanation
As explained in the example.

Time Limit(X):
0.50 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3

'''


import numpy as np

def solver(p,d,inputList):

    sum = 0
    for i in range(0,p):
        



def main():
    pd = list(map(int,input().strip().split()))
    p = pd[0]
    d = pd[1]

    tempList =[[]*p]*d
    
    for i in range(0,d):
        tempList[i] = list(map(int,input().strip().split()))

    inputList= np.array(tempList)

    output = solver(p,d,inputList)
    
main()


