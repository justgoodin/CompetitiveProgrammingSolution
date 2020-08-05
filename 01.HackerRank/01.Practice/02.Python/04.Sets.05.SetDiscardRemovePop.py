#Link to the question below
#

#I'm cheating with try/except, but the KeyError irritiated me

n = int(input())
s = set(map(int, input().split()))
steps = int(input())
comm = {"pop":s.pop,"remove":s.remove,"discard":s.discard}


for i in range(steps):
    try:
        c = input().split()
        comm[c[0]](int(c[1])) if len(c)>1 else comm[c[0]]()
    except KeyError:
        continue

print(sum(s))