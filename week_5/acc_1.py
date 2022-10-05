line1 = [1, 2, 3]
line2 = [4, 5 ,6]
line3 = [7, 8, 9]

chessTable = [line1,line2,line3]

size = 3

def printBoard():
    printLine(line1)
    printLine(line2)
    printLine(line3)

def printLine(line):
    for i in range(len(line)):

        if i < len(line)-1:
            print("|",line[i],"|", end="")
        else:
            print("|",line[i],"|")

def xTurn():
    position = int(input("X: "))
    if(isRepeat(position)):
        print("Error: N/A position")
        printBoard()
        xTurn()
    elif(type(position) != int or position > 9 or position < 1 ):
        print("Error: invalid input")
        printBoard()
        xTurn()
    else:
        if(position >= 1 and position <= 3):
            line1.remove(position)
            line1.insert(position-1,"X")
        if(position >= 4 and position <= 6):
            line2.remove(position)
            line2.insert(position-4,"X")
        if(position >= 7 and position <= 9):
            line3.remove(position)
            line3.insert(position-7,"X")

def oTurn():
    position = int(input("O: "))
    if(isRepeat(position)):
        print("Error: N/A position")
        printBoard()
        oTurn()
    elif(type(position) != int or position > 9 or position < 1 ):
        print("Error: invalid input")
        printBoard()
        oTurn()
    else:
        if(position >= 1 and position <= 3):
            line1.remove(position)
            line1.insert(position-1,"O")
        if(position >= 4 and position <= 6):
            line2.remove(position)
            line2.insert(position-4,"O")
        if(position >= 7 and position <= 9):
            line3.remove(position)
            line3.insert(position-7,"O")

def isRepeat(position):
    if(position >= 1 and position <= 3):
        if line1[position-1] == "O" or line1[position-1] == "X":
            return True
        else:
            return False
    if(position >= 4 and position <= 6):
        if line2[position-4] == "O" or line2[position-4] == "X":
            return True
        else:
            return False
    if(position >= 7 and position <= 9):
        if line3[position-7] == "O" or line3[position-7] == "X":
            return True
        else:
            return False

def checkStatus(side):
    for i in range(0,size):
        count = 0
        for j in range(0,size):
            if chessTable[i][j] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True

    for i in range(0,size):
        count = 0
        for j in range(0,size):
            if chessTable[j][i] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    if chessTable[0][0] == side:
        count = 0
        for i in range(0,size):
            if chessTable[i][i] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    if chessTable[0][size-1] == side:
        count = 0
        for i in range(0,size):
            if chessTable[i][size-i-1] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    return False

def isFull():

    for i in range(3):
        for j in range(3):
            if str(chessTable[i][j]).isdigit():
                return False
    
    return True

printBoard()

while(True):
    xTurn()
    printBoard()
    if(checkStatus("X")):
        print("Player X wins")
        break
    if(isFull()):
        print("Tie")
        break
    oTurn()
    printBoard()
    if(checkStatus("O")):
        print("Player O wins")
        break
    if(isFull()):
        print("Tie")
        break