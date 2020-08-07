#Link to the question below
#https://www.techgig.com/practice/question/kirana-store/YUxZY2kxVFZjT25qSkh4UHlDb0tiWmtuQmtxZDRrdGhld0dVdE9tcVIxL2dHb3Z4SngvbTJGOE5jY2FwQXZjUw==/1


from collections import Counter

def main():
    N = int(input())
    items = Counter(list(map(int,input().split())))
    C = int(input())
    #inventory = items.most_common()
    sales = 0
    for i in range(C):
        item,price = map(int,input().split())
        if items[item]>0:
            items.subtract({item:1})
            sales += price
    
    print(sales)

main()


