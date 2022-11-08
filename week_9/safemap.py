biglist = []
finallist = []

def inputlist():
    n = input()
    length = 1
    list = []
    for number in n:
        list.append(number)
    biglist.append(list)
    
    while length != len(n):
        list = []
        n = input()
        for number in n:
            list.append(number)
        biglist.append(list)
        length+= 1

def expand():
    for a in biglist:
        a.insert(0, '0')
        a.insert(0, '0')
        a.append('0')
        a.append('0')
    biglist.insert(0, [str(0)]*(len(biglist[0])))
    biglist.insert(0, [str(0)]*(len(biglist[0])))
    biglist.append([str(0)]*len(biglist[0]))
    biglist.append([str(0)]*len(biglist[0]))

def safe(a, b):
    for c in range(a-1, a+2): 
        for d in range(b-1, b+2): 
            if biglist[c][d] == '1':
                return False
    return True

def supersafe(a, b):
    for c in range(a-2, a+3):
        for d in range(b-2, b+3):
            if biglist[c][d] == '1':
                return False
    return True

def check():
    row = len(biglist)
    for a in range(2, row-2):
        list2 = []
        for b in range(2, row-2):
            if biglist[a][b] == '1': #dangerous chemical
                list2.append('#')
            else: #b = 0
                if safe(a, b):
                    if supersafe(a, b):
                        list2.append('2')
                    else:
                        list2.append('1')
                else:
                    list2.append('0')

        finallist.append(list2)
    return finallist

def printboard():
    for a in finallist:
        a = ''.join(a)
        print(a)

def main():
    inputlist()
    expand() #expand the map
    # 11
    # 11
    # 000000
    # 000000
    # 001100
    # 001100
    # 000000
    # 000000
    check()
    printboard()

main()
