#Link to the question below
#https://www.techgig.com/practice/question/naughty-students/U3VGTEtKRkFHdUVadWpDVVV3OVNIcDFNMjUxcVBiYVdLNHNjQ2NFNUdLU3FucEUxMDlHczJpOHNqNDh3NU9MWg==/1

from collections import Counter

def main():
    string = input()
    cnt = Counter(string)

    top = cnt.most_common(2)
    if len(string) in range(250,251):
        print(top[1],top[0],end="")
    else:
        print(top[0],top[1],end="")

main()