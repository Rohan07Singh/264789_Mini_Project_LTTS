def resetBoard():
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }
    return theBoard

def checkTheBoard(theBoard):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
        return True        
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
        return True
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
        return True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
        return True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
        return True
    else:
        return False

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    f = open("final_tictactoe.txt", "w")
    f.write(board['7'] + '|' + board['8'] + '|' + board['9']+ '\n')
    f.write('-+-+-'+ '\n')
    f.write(board['4'] + '|' + board['5'] + '|' + board['6']+ '\n')
    f.write('-+-+-'+ '\n')
    f.write(board['1'] + '|' + board['2'] + '|' + board['3']+ '\n')
    f.close()

def game():

    turn = 'X'
    count = 0
    theBoard = resetBoard()

    while True:
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if checkTheBoard(theBoard) == True:
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":  
        game()

if __name__ == "__main__":
    game()