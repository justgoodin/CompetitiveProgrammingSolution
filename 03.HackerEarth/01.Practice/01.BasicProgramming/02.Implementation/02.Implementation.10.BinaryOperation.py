#Link to the question below
#

if __name__ == "__main__":
    T = int(input())

    c0,c1,c2,c3=input().split()
    d={'00':c0,'01':c1,'10':c2,'11':c3}
    if d[c0+'0']!=d['0'+c0] or d[c0+'1']!=d['0'+c1] or d[c1+'0']!=d['0'+c2] or d[c1+'1']!= d['0'+c3] or d[c2+'0']!=d['1'+c0] or d[c2+'1']!= d['1'+c1] or d[c3+'0']!=d['1'+c2] or d[c3+'1']!=d['1'+c3]:
        print('No')
    else:
        print('Yes)