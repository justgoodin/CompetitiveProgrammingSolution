#Link to the question below
#https://www.techgig.com/practice/question/club-entry/ZFNyS1BoWFppZnhraW91ei9UUjRYQnVpYWVtRVZ5SzVlRnFNcjNuUkk0WThaUkFrY0FqNlB3WURGR3U3YmdEcQ==/1

def main():

    num = input()
    output = "null"

    if len(set(num))== len(num):
        output="DO NOT ENTER"
    else:
        output = "ENTER"

    print(output)

main()