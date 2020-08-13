#Link to the question below
#https://www.hackerrank.com/challenges/30-inheritance/problem?isFullScreen=true

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # 	Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # 	Write your function here
    
	def calculate(self):
        size = len(scores)
        average = sum(scores)//size
        grade = str()

        if average in range(90,100+1):
            grade = "O"
        elif average in range(80,90):
            grade = "E"
        elif average in range(70,80):
            grade = "A"
        elif average in range(55,70):
            grade = "P"
        elif average in range(40,55):
            grade = "D"
        else:
            grade = "T"

        return grade
        
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())