#Link to the question below
#

def main():

   count = int(input())
   score = []
    
   for i in range(0,count):
      score.append(int(input())) 
	  
   print(max(score))

main()