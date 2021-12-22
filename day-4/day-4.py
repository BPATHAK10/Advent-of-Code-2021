from typing import DefaultDict
from pprint import pprint

def checkWin(board):
    # check rows
    for row in board:
        rowFlag = True
        for elem in row:
            if elem != "X":
                rowFlag = False
        if rowFlag:
            break

    # check columns
    for i in range(5):
        colFlag = True
        for j in range(5):
            if board[j][i] != "X":
                colFlag = False
        if colFlag:
            break
    
    return rowFlag or colFlag
         
def findSumUpdated(board):
    numbersList = [int(num) for ls in board for row in ls for num in row if num != "X"]
    return sum(numbersList)

       
def findSum(board):
    numbersList = [int(num) for row in board for num in row if num != "X"]
    return sum(numbersList)


def partOne():
    with open("./day-4/data.txt","r") as file:
        lines = file.readlines()

    l = [ ln.strip().split() for ln in lines]
    # print(l)

    numCalls = l[0][0].split(",")
    # print("number calls is :::",numCalls)

    boardsRows = [ row for row in l if len(row)==5]
    # print(boardsRows)

    noOfBoards = int(len(boardsRows)/5)
    wonBoard = []
    isBoardWon = False
    lastNumCall = int()

    boards = DefaultDict(list)

    num = 0
    for i in range(len(boardsRows)):
        boards[num].append(boardsRows[i]) 
        if (i+1) % 5 == 0:
            num += 1

    # pprint(boards)
    markedBoards = DefaultDict(list)

    for num in numCalls:
        if isBoardWon:
            break
        for board in boards.values():
            for row in board:
                if num in row:
                    num_index = row.index(num)
                    # print(num, "found in row :: ", row, " at index ::", row.index(num))
                    # row.replace(row.index(num), "X")
                    row.remove(num)
                    row.insert(num_index,"X")
                    # print(row, "\n")
            isBoardWon = checkWin(board)
            # print(isBoardWon)
            if isBoardWon:
                wonBoard = board
                lastNumCall = int(num)
                break

        # print(f"Boards after {num}")
        # pprint(boards)

    print("the winning board is ::")
    pprint(wonBoard)

    returningSum = findSum(wonBoard)
    # print(returningSum)

    # print("last num call is ::",lastNumCall)

    print("answer :: ", returningSum*lastNumCall)
        

def partTwo():
    with open("./day-4/data.txt","r") as file:
        lines = file.readlines()

    l = [ ln.strip().split() for ln in lines]
    # print(l)

    numCalls = l[0][0].split(",")
    # print("number calls is :::",numCalls)

    boardsRows = [ row for row in l if len(row)==5]
    # print(boardsRows)

    noOfBoards = int(len(boardsRows)/5)
    lastWonBoard = []
    isBoardWon = False
    lastNumCall = int()

    boards = DefaultDict(list)

    num = 0
    for i in range(len(boardsRows)):
        boards[num].append(boardsRows[i]) 
        if (i+1) % 5 == 0:
            num += 1

    # pprint(boards)
    markedBoards = DefaultDict(list)

    for num in numCalls:
        boardIndex = 0
        if isBoardWon and len(boards)==0:
            break
        for key, board in dict(boards).items():
            for row in board:
                if num in row:
                    num_index = row.index(num)
                    # print(num, "found in row :: ", row, " at index ::", row.index(num))
                    # row.replace(row.index(num), "X")
                    row.remove(num)
                    row.insert(num_index,"X")
                    # print(row, "\n")
            isBoardWon = checkWin(board)
            # print(isBoardWon)
            lastNumCall = int(num)
            if isBoardWon:
                boards.pop(key)
                if len(boards) == 0:
                    lastWonBoard = board
                    break

            boardIndex += 1

        # print(f"Boards after {num}")
        # pprint(boards)

    # print("the remaing board is ::")
    # pprint(boards)

    # returningSum = findSumUpdated(boards.values())
    returningSum = findSum(lastWonBoard)
    print(returningSum)

    print("last num call is ::",lastNumCall)

    print("answer :: ", returningSum*lastNumCall)
        


def main():
    partTwo()

if __name__ == "__main__":
    main()