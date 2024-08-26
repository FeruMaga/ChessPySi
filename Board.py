from Pieces import *

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)] 
        self.init() 
        self.turn = 0
        self.blackCapture = []
        self.whiteCapture = []

    def init(self):
        self.board[0][0] = Rook((0, 0), 'White')
        self.board[0][1] = Knight((0, 1), 'White')
        self.board[0][2] = Bishop((0, 2), 'White')
        self.board[0][3] = Queen((0, 3), 'White')
        self.board[0][4] = King((0, 4), 'White')
        self.board[0][5] = Bishop((0, 5), 'White')
        self.board[0][6] = Knight((0, 6), 'White')
        self.board[0][7] = Rook((0, 7), 'White')

        self.board[7][0] = Rook((7, 0), 'Black')
        self.board[7][1] = Knight((7, 1), 'Black')
        self.board[7][2] = Bishop((7, 2), 'Black')
        self.board[7][3] = Queen((7, 3), 'Black')
        self.board[7][4] = King((7, 4), 'Black')
        self.board[7][5] = Bishop((7, 5), 'Black')
        self.board[7][6] = Knight((7, 6), 'Black')
        self.board[7][7] = Rook((7, 7), 'Black')

        for col in range(8):
            self.board[1][col] = Pawn((1, col), 'White')
            self.board[6][col] = Pawn((6, col), 'Black')

    # White Turn = 0
    # Black Turn = 1
    def nextTurn(self):
        self.turn = 1 - self.turn

    def getTurn(self):
        return self.turn
    
    def getPiece(self, coordinates):
        y = coordinates[1]
        x = coordinates[0]
        piece = self.board[int(x)][int(y)]
        if piece != None:
            print(piece)
            return piece

        return None
    
    def getPieceByName(self, name):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].__str__() == name:
                    piece = self.board[row][col]
                    return piece
                
        return
    
    def updateMove(self, piece, newMove):
        oldPosition = piece.getPosition()
        print("Update move board old positon:")
        print(oldPosition)
        self.board[oldPosition[0]][oldPosition[1]] = 0
        piece.updateMove(newMove)
        print("Update move board new positon:")
        
        print(newMove)
        self.board[newMove[0]][newMove[1]] = piece

    def capture(self, piece):
        position = piece.getPosition()
        piece.captured()
        self.board[position[0]][position[1]] = 0

        if piece.color == "White":
            self.blackCapture.append(piece)
        elif piece.color == "Black":
            self.whiteCapture.append(piece)

    def check(self):

        turn = self.getTurn()

        if turn:
            print("Black King")
            king = self.getPieceByName("King Black")
            color = "White"
        elif not turn:
            print("White King")
            king = self.getPieceByName("King White")
            color = "Black"
        else:
            raise ValueError("Invalid turn value!")

        if king is None:
            raise ValueError(f"King not found on the board!")
        
        positionKing = king.position

        print(positionKing)

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                
                if piece and piece.color == color:
                    if piece.isPossibleMove(self.board, positionKing):
                        return True
                
        return False
    
