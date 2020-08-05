#Link to the question below
#

m,n = map(int,input().strip().split())

symbol = ".|."

for i in range(1,(int(m/2)+1)):
    print(((2*i-1)*symbol).center(n,"-"))

print("WELCOME".center(n,"-"))

for j in range(1,(int(m/2)+1)):
    i = int(m/2)+1-j
    print(((2*i-1)*symbol).center(n,"-"))