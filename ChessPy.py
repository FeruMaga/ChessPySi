from Pieces import *

import sys
import os
import re

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)] 
        self.init() 
        self.turn = 0

    def init(self):
        self.board[0][0] = Rook((0, 0), 'Black')
        self.board[0][1] = Knight((0, 1), 'Black')
        self.board[0][2] = Bishop((0, 2), 'Black')
        self.board[0][3] = Queen((0, 3), 'Black')
        self.board[0][4] = King((0, 4), 'Black')
        self.board[0][5] = Bishop((0, 5), 'Black')
        self.board[0][6] = Knight((0, 6), 'Black')
        self.board[0][7] = Rook((0, 7), 'Black')

        self.board[7][0] = Rook((7, 0), 'White')
        self.board[7][1] = Knight((7, 1), 'White')
        self.board[7][2] = Bishop((7, 2), 'White')
        self.board[7][3] = Queen((7, 3), 'White')
        self.board[7][4] = King((7, 4), 'White')
        self.board[7][5] = Bishop((7, 5), 'White')
        self.board[7][6] = Knight((7, 6), 'White')
        self.board[7][7] = Rook((7, 7), 'White')

        for col in range(8):
            self.board[1][col] = Pawn((1, col), 'Black')
            self.board[6][col] = Pawn((6, col), 'White')

    def nextTurn(self):
        self.turn = 1 - self.turn

    def getTurn(self):
        return self.turn

def displayGame(board):
    print("  -----------------")
    for i in range(8):
        row_str = str(8 - i) + " |"
        for j in range(8):
            piece = board.board[i][j]
            if piece == 0:
                if (i + j) % 2 == 0:
                    row_str += "_|"
                else:
                    row_str += "#|"
            else:
                if piece.__str__() == 'Pawn Black':
                    row_str += "♟|"
                elif piece.__str__() == 'Pawn White':
                    row_str += "♙|"
                elif piece.__str__() == 'Rook Black':
                    row_str += "♜|"
                elif piece.__str__() == 'Rook White':
                    row_str += "♖|"
                elif piece.__str__() == 'Knight Black':
                    row_str += "♞|"
                elif piece.__str__() == 'Knight White':
                    row_str += "♘|"    
                elif piece.__str__() == 'Bishop Black':
                    row_str += "♝|"
                elif piece.__str__() == 'Bishop White':
                    row_str += "♗|"    
                elif piece.__str__() == 'Queen Black':
                    row_str += "♛|"
                elif piece.__str__() == 'Queen White':
                    row_str += "♕|"    
                elif piece.__str__() == 'King Black':
                    row_str += "♚|"
                elif piece.__str__() == 'King White':
                    row_str += "♔|"    
        print(row_str)
    print("  ----------------")
    print("   a b c d e f g h")



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
    if(len(steps) == 2):
        newcoordenates = []
        coordenates1 = steps[0] 
        coordenates2 = steps[1]
        letter1 = coordenates1[0]
        letter2 = coordenates2[0]
        if(letter1.isalpha() and letter2.isalpha()):
            number1 = ord(letter1) - 96
            number2 = ord(letter2) - 96
            x = str(number1) + coordenates1[1]
            y = str(number2) + coordenates2[1]
            newcoordenates.append(x)
            newcoordenates.append(y)
            print(x)
            print(y)
            return newcoordenates
        else:   
            print("Please first the letter then the number.")
            return
        
def GameOver():
    return False



def game():
    steps = []
    board = Board()
    board.init()
    print("Write the coordenates of your piece, then the coordenates for where it would be. \nExample: e2 e4")
    displayGame(board=board)
    turn = 0
    while not GameOver():
        step = input()
        steps = re.findall(r"[\w]+", step)
        if(len(steps) == 2):
            if(not board.getTurn()):
                translateLetter(steps)   
            elif(board.getTurn()):
                translateLetter(steps)
            else:
                print("Error: Turn")
        else:
            clean()
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
            break
        elif choose == "2":
            print("Player vs AI choosed!")
            break
        elif choose == "0":
            sys.exit()
        else: 
            print("\nThis option does not exist, try again.\n")

    clean()
    game()


if __name__ == '__main__':
    main()


