#Link to the question below
#https://www.techgig.com/practice/question/name/L01mNFNPeUpMRGJocjk0bU9JS0ZEMDFkRUExbERSSUloa3BmWlhZNkRkeTRwMmswZFpRaENIZDlHd28veUx2Tw==/1

def main():
    name = input()
    invalid = ["w","y","z","x","i"]
    output = "YES"

    for i in name:
        if i in invalid:
            output = "NO"
    
    print(output)

main()