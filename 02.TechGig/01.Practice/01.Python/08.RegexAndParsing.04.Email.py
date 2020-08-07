#Link to the question below
#https://www.techgig.com/practice/question/e-mail/K1dQdkRiMnp5K0ptMUlKVUwwL0lGbVVNN0gxbTF2dHhhdlVscTZxbXkxSVN2bFpDSkNNdXVzbjE1ckdsYTNxVw==/1

def main():

    email = input()
    output = str()

    if "@" in email and email[-4:]==".com":
        output = "YES"
    else:
        output = "NO"

    print(output)
    
main()