#Link to the question below
#

def count_substring(string, sub_string):
    sizeString = len(string)
    sizeSubString  = len(sub_string)
    count = 0

    for i in range(sizeString-sizeSubString+1):
        if string[i:i+sizeSubString]==sub_string:
            count += 1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)