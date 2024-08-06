import sys

class Piece(object):
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __str__(self) -> str:
        return self.color
    
class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Pawn ' + super().__str__()

class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Rook ' + super().__str__()

class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Knight '+ super().__str__()

class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

    def __str__(self) -> str:
        return 'Bishop ' + super().__str__()
    
class Queen(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
    
    def __str__(self) -> str:
        return 'Queen ' + super().__str__()

class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
              
    def __str__(self) -> str:
        return 'King ' + super().__str__()

def initGame():
        
    board = [[0 for _ in range(8)] for _ in range(8)]

    board[0][0] = Rook((0, 0), 'Black')
    board[0][1] = Knight((0, 1), 'Black')
    board[0][2] = Bishop((0, 2), 'Black')
    board[0][3] = Queen((0, 3), 'Black')
    board[0][4] = King((0, 4), 'Black')
    board[0][5] = Bishop((0, 5), 'Black')
    board[0][6] = Knight((0, 6), 'Black')
    board[0][7] = Rook((0, 7), 'Black')

    board[7][0] = Rook((7, 0), 'White')
    board[7][1] = Knight((7, 1), 'White')
    board[7][2] = Bishop((7, 2), 'White')
    board[7][3] = Queen((7, 3), 'White')
    board[7][4] = King((7, 4), 'White')
    board[7][5] = Bishop((7, 5), 'White')
    nome = board[7][5] 
    print(nome.__str__)
    board[7][6] = Knight((7, 6), 'White')
    board[7][7] = Rook((7, 7), 'White')

    for col in range(8):
        board[1][col] = Pawn((1, col), 'Black')
        board[6][col] = Pawn((6, col), 'White')

    displayGame(board=board)

def displayGame(board):
    print("   a b c d e f g h")
    print("  -----------------")
    for i in range(8):
        row_str = str(8 - i) + " |"
        for j in range(8):
            piece = board[i][j]
            if piece == 0:
                if (i + j) % 2 == 0:
                    row_str += "_|"
                else:
                    row_str += "#|"
            else:
                if piece.__str__() == 'Pawn Black':
                    row_str += "♟︎|"
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



def gameStart(): 
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
        elif choose == "3":
            sys.exit()
        else: 
            print("\nThis option does not exist, try again.\n")

    initGame()


if __name__ == '__main__':
    gameStart()


