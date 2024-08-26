from Board import *
from Pieces import *

import sys
import os
import re


def displayGame(board):

    displayCapture(board)

    print("  -----------------")
    for y in range(7, -1, -1):
        row_str = str(y + 1) + " |"
        for x in range(8):
            piece = board.board[x][y]
            if piece == 0:
                if (x + y) % 2 == 0:
                    row_str += "_|"
                else:
                    row_str += "#|"
            else:
                if piece.__str__() == 'Pawn White':
                    row_str += "♟|"
                elif piece.__str__() == 'Pawn Black':
                    row_str += "♙|"
                elif piece.__str__() == 'Rook White':
                    row_str += "♜|"
                elif piece.__str__() == 'Rook Black':
                    row_str += "♖|"
                elif piece.__str__() == 'Knight White':
                    row_str += "♞|"
                elif piece.__str__() == 'Knight Black':
                    row_str += "♘|"    
                elif piece.__str__() == 'Bishop White':
                    row_str += "♝|"
                elif piece.__str__() == 'Bishop Black':
                    row_str += "♗|"    
                elif piece.__str__() == 'Queen White':
                    row_str += "♛|"
                elif piece.__str__() == 'Queen Black':
                    row_str += "♕|"    
                elif piece.__str__() == 'King White':
                    row_str += "♚|"
                elif piece.__str__() == 'King Black':
                    row_str += "♔|"    
        print(row_str)
    print("  ----------------")
    print("   a b c d e f g h")

def displayCapture(board):
        rowWhitePiece = ""
        rowBlackPiece = ""

        if board.blackCapture or board.whiteCapture:
            print("White captures: ")
            if board.whiteCapture:
                for piece in board.whiteCapture:
                    if piece.__str__() == 'Pawn Black':
                        rowBlackPiece += " ♙"
                    elif piece.__str__() == 'Rook Black':
                        rowBlackPiece += " ♖"
                    elif piece.__str__() == 'Knight Black':
                        rowBlackPiece += " ♘"    
                    elif piece.__str__() == 'Bishop Black':
                        rowBlackPiece += " ♗"    
                    elif piece.__str__() == 'Queen Black':
                        rowBlackPiece += " ♕"    
                    elif piece.__str__() == 'King Black':
                        rowBlackPiece += " ♔"    
            print(rowBlackPiece)
            print("Black captures: ")
            if board.blackCapture:
                for piece in board.blackCapture:
                    if piece.__str__() == 'Pawn White':
                        rowWhitePiece += "♟|"
                    elif piece.__str__() == 'Rook White':
                        rowWhitePiece += "♜|"
                    elif piece.__str__() == 'Knight White':
                        rowWhitePiece += "♞|"
                    elif piece.__str__() == 'Bishop White':
                        rowWhitePiece += "♝|"  
                    elif piece.__str__() == 'Queen White':
                        rowWhitePiece += "♛|"
                    elif piece.__str__() == 'King White':
                        rowWhitePiece += "♚|"

            print(rowWhitePiece)


def clean():
    try:
        clear = lambda: os.system('clear')
        clear()
    except:
        pass

    try:
        clear = lambda: os.system('cls')
        clear()
    except:
        pass


def translateLetter(steps):
    if len(steps) == 2 and steps[0][1].isnumeric() and steps[1][1].isnumeric() and steps[0][0].isalpha() and steps[1][0].isalpha():
        currentLetterLower =  steps[0][0].lower()
        newMoveLetterLower = steps[1][0].lower()
        currentStateLetter = int(ord(currentLetterLower) - 96) - 1
        currentStateNumber = int(steps[0][1]) - 1 
        newMoveLetter =  int(ord(newMoveLetterLower) - 96) - 1
        newMoveNumber = int(steps[1][1]) -1
        try:
            if currentStateLetter < 8 and  currentStateNumber < 8 and newMoveLetter < 8 and newMoveNumber < 8:
                newcoordinates = [
                    currentStateLetter,currentStateNumber,
                    newMoveLetter,newMoveNumber
                ]
                return newcoordinates
            else:
                print("Coordinates out of range, please provide valid coordinates.")
        except IndexError:
            print("Please provide valid coordinates.")
    else:   
        print("Coordinates not recognized, try again.")
        

def move(board, steps):
    currentState = steps[0:2]
    newMove = steps[2:4]
    piece = board.getPiece(currentState)

    if not piece:
        print("No piece choosed!")
        return 
    
    if board.getTurn() and piece.color == "White" or not board.getTurn( ) and piece.color == "Black":
            print("It is not your turn!")
            return
    
    if piece.isPossibleMove(board, newMove):

        oldPosition = piece.getPosition()
        pieceCapture = board.getPiece(newMove)
        board.updateMove(piece, newMove)

        if board.check():
            print("Move results in check!")
            board.updateMove(piece, oldPosition)
            return
        
        
        if pieceCapture:
            board.capture(pieceCapture)

        board.nextTurn()
    else:
        print("This is not a possible move, try again.")
        return

def GameOver(board):
    if board.checkMate:
        return True
    else:
        return False



def game():
    steps = []
    board = Board()
    print("Write the coordenates of your piece, then the coordenates for where it would be. \nExample: e2 e4")
    print("If want to exit, write 0.")
    
    turn = 0
    while not GameOver(board):

        if board.getTurn() == 0:
            print("White Turn!\n")
        else:
            print("Black Turn!\n")

        displayGame(board)
        
        step = input()
        steps = re.findall(r"[\w]+", step)
        
        if(len(steps) == 2):
            stepsTranslated = translateLetter(steps)
            if stepsTranslated:
                move(board, stepsTranslated)

                if board.checkmate():
                    print(f"Checkmate! {'White' if board.getTurn() == 1 else 'Black'} wins!")
                    break
                
        elif step == '0':
            sys.exit()
        else:
            print("Coordenates not recognized, try again.")
            displayGame(board=board)
        


def main(): 
    print("                       Welcome ChessPy")
    print(r"""
                                                        _:_
                                                        '-.-'
                                            ()      __.'.__
                                            .-:--:-.  |_______|
                                    ()      \____/    \=====/
                                    /\      {====}     )___(
                        (\=,      //\\      )__(     /_____\
        __    |'-'-'|  //  .\    (    )    /____\     |   |
        /  \   |_____| (( \_  \    )__(      |  |      |   |
        \__/    |===|   ))  `\_)  /____\     |  |      |   |
        /____\   |   |  (/     \    |  |      |  |      |   |
        |  |    |   |   | _.-'|    |  |      |  |      |   |
        |__|    )___(    )___(    /____\    /____\    /_____\
        (====)  (=====)  (=====)  (======)  (======)  (=======)
        }===={  }====={  }====={  }======{  }======{  }======={
    (______)(_______)(_______)(________)(________)(_________)
    """)
    while True:
        print("Choose the type of game:")
        print("Player vs Player [1]")
        print("Player vs AI [2]")
        print("Exit [0]")

        choose = input()

        if choose == "1":
            print("Player vs Player choosed! ")
            clean()
            game()
            break
        elif choose == "2":
            print("Player vs AI choosed!")
            clean()
            game()
            break
        elif choose == "0":
            sys.exit()
        else: 
            print("\nThis option does not exist, try again.\n")




if __name__ == '__main__':
    main()


