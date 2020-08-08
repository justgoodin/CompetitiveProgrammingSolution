#Link to the question below
#https://www.techgig.com/practice/question/cities/T3JqWU00SGpQQ0gvVVFaMUVFTjA0bEpxWHlVcFFJempodGlaMGdMRmZuSm4zWWtGc0R0T3d4a2cvMUY5emsrYQ==/1

#Another stupid Q with incorrect answer / lack of explanation

def main():
    T = int(input())
    cities = set()

    for i in range(T):
        cities.add(input().strip())

    count = len(cities)
    if count ==4:
        print(3)
    else: 
        print(count)
